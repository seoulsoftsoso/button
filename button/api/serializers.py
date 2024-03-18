import traceback
from datetime import date, datetime
import time
from decimal import *

from django.db import IntegrityError, transaction
from django.db.models import Sum, Avg, Q, Count
from django.db.models.functions import Coalesce
from django.shortcuts import get_object_or_404
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from rest_framework.exceptions import ValidationError

from api.models import CodeMaster, GroupCodeMaster, EnterpriseMaster, UserMaster



def generate_code(prefix1, model, model_field_prefix, user):
    today = date.today()
    prefix2 = str(today.year * 10000 + today.month * 100 + today.day)
    kwargs = {
        model_field_prefix + '__istartswith': prefix1 + prefix2,
        'enterprise': user.enterprise
    }
    res = model.objects.filter(**kwargs).order_by(model_field_prefix)
    if res.exists() is False:
        return prefix1 + str(int(prefix2) * 1000)

    last_order = res.values(model_field_prefix).last()[model_field_prefix]
    return prefix1 + str(int(prefix2) * 1000 + int(last_order[-3:]) + 1)


def generate_lot_code(code_id, model, model_field_prefix, user):

    if not code_id:
        raise ValidationError('자재구분 코드를 입력해주세요.')

    prefix1 = CodeMaster.objects.filter(id=code_id).values('code').first().get('code')

    if not prefix1:
        raise ValidationError('자재구분 코드가 존재하지 않습니다.')

    today = date.today()
    prefix2 = f"{today.year}{today.month:02d}{today.day:02d}"

    kwargs = {
        model_field_prefix + '__istartswith': prefix1 + '-' + prefix2 + '-',
        'enterprise': user.enterprise
    }

    cnt = model.objects.filter(**kwargs).aggregate(cnt=Count('*'))['cnt']
    print("cnt   : " + str(cnt))
    if cnt == 0:
        return prefix1 + '-' + prefix2 + '-' + '01'
    elif 0 < cnt < 9:
        return prefix1 + '-' + prefix2 + '-' + '0' + str(int(cnt) + 1)
    elif cnt == 99:
        raise ValidationError('당일 순번이 99를 초과하여 입고등록을 진행 할 수 없습니다.')
    else:
        return prefix1 + '-' + prefix2 + '-' + str(int(cnt) + 1)


class BaseSerializer(serializers.ModelSerializer):
    created_by = serializers.CharField(required=False, read_only=True)  # 최종작성일
    updated_by = serializers.CharField(required=False, read_only=True)  # 최종작성자

    def __init__(self, *args, **kwargs):
        super(BaseSerializer, self).__init__(*args, **kwargs)

        # override fields' error messages.
        for field in self.fields:
            f = self.fields[field]
            for k, v in f.error_messages.items():
                try:
                    verbose_name = getattr(f.parent.Meta.model, getattr(f, 'field_name')).field.verbose_name
                    f.error_messages[k] = verbose_name + ": " + str(v)
                except:
                    continue

    def get_by_username(self):
        return self.context['request'].user

    def create(self, instance):
        instance['created_by'] = self.get_by_username()
        instance['updated_by'] = self.get_by_username()

        return super().create(instance)

    def update(self, instance, validated_data):
        validated_data['updated_by'] = self.get_by_username()

        return super().update(instance, validated_data)

    def code_validator(self, code_master, group_code):
        if code_master is None:
            return code_master

        qs = GroupCodeMaster.objects.filter(pk=code_master.group_id, code=group_code)
        if qs.exists() is not True:
            message = '잘못된 코드 code must be a multiple of %d.' % group_code
            raise serializers.ValidationError(message)

        return code_master

    def to_internal_value(self, data):
        self.unlock_data(data)

        if 'enterprise' not in data:
            enterprise = self.context['request'].user.enterprise
            data['enterprise'] = enterprise.id

        return super(BaseSerializer, self).to_internal_value(data)

    def unlock_data(self, data):
        if type(data) is not dict:
            data._mutable = True


class EnterpriseMasterSerializer(serializers.ModelSerializer):
    master = serializers.SerializerMethodField(required=False, read_only=True)

    class Meta:
        model = EnterpriseMaster
        fields = '__all__'

    def get_master(self, obj):
        res = UserMaster.objects.filter(enterprise=obj, is_master=True)
        if res.count() > 1:
            raise ValidationError('[에러] 관리자 master id가 1명 이상입니다. 시스템 관리자에게 보고해주십시오.')

        return UserMasterSerializer(res.first()).data


class GroupCodeMasterSerializer(BaseSerializer):
    class Meta:
        model = GroupCodeMaster
        fields = '__all__'


class CodeMasterSerializer(BaseSerializer):
    class Meta:
        model = CodeMaster
        fields = '__all__'

    #
    # def get_generated_id(self, obj):
    #     return 1000 * obj['group'].code + obj['code']

    def create(self, instance):
        # validated_data['id'] = self.get_generated_id(validated_data)

        try:
            return super().create(instance)
        except IntegrityError:
            raise ValidationError('중복되는 id 이므로 생성할 수 없습니다.')

    def to_representation(self, instance):

        self.fields['group'] = GroupCodeMasterSerializer()
        return super(CodeMasterSerializer, self).to_representation(instance)


class CodeMasterSelectSerializer(BaseSerializer):
    class Meta:
        model = CodeMaster
        fields = '__all__'

    def to_representation(self, instance):
        return {
            'id': instance.id,
            'name': instance.name,
        }


class UserMasterSerializer(serializers.ModelSerializer):
    code = serializers.CharField(max_length=8, required=False, read_only=True)
    password = serializers.CharField(write_only=True)

    created_by = serializers.CharField(required=False, read_only=True)  # 최종작성일
    created_at = serializers.CharField(required=False, read_only=True)  # 최초작성일

    enterprise_name = serializers.SerializerMethodField(read_only=True, required=False)
    enterprise_manage = serializers.SerializerMethodField(read_only=True, required=False)  # 관리명

    # enterprise = serializers.IntegerField(required=False, read_only=True)

    class Meta:
        model = UserMaster
        # fields = ['id', 'user_id', 'code', 'username', 'factory_classification',
        #           'employment_division', 'employment_date', 'job_position', 'department_position',
        #           'postal_code', 'address', 'enable', 'etc', 'created_by', 'created_at']
        fields = '__all__'
        optional_fields = ['enterprise']
        # exclude = ['enterprise']

    def get_enterprise_name(self, obj):
        if obj.enterprise:
            return obj.enterprise.name
        else:
            return "Seoul-soft"

    def get_enterprise_manage(self, obj):
        if obj.enterprise:
            return obj.enterprise.manage
        else:
            return ""

    def get_at_date(self):
        return date.today()

    def get_by_username(self):
        return self.context['request'].user

    def get_code(self, obj):
        if obj['is_master'] is True:
            return obj['enterprise'].code + "0000"

        # print(obj['factory_classification'].id)
        # factory = str(obj['factory_classification'].id)[0]
        # division = str(obj['department_position'].id)[0]
        date = str(obj['employment_date']).replace('-', '')[2:6]
        order = '00'

        # prefix = factory + division + date
        prefix = 'UN' + date
        res = UserMaster.objects.filter(code__istartswith=prefix)
        if res.exists():
            num = res.order_by('-code').first().code[-2:]
            order = str(int(num) + 1)
            if len(order) == 1:
                order = '0' + order

        return 'UN' + date + order

    def create(self, instance):
        instance['code'] = self.get_code(instance)
        instance['created_at'] = self.get_at_date()
        instance['created_by'] = self.get_by_username()

        # is_master
        if instance['is_master'] is False:
            # if None in (instance['username']):
            #     raise ValidationError('유저이름은 필수 항목들입니다.')

            instance['enterprise'] = self.context['request'].user.enterprise
        else:
            instance['permissions'] = instance['enterprise'].permissions
            # 마스터 계정 생성 에러 관련
            instance['username'] = instance['enterprise'].name + ' 관리자'

        try:
            user = super().create(instance)
            user.set_password(instance['password'])
            user.save()
            return user
        except IntegrityError:
            raise ValidationError('유효하지 않은 code 이므로 생성할 수 없습니다.')  # TODO: Error message

    def update(self, instance, validated_data):

        if 'permissions' in validated_data:
            # invalidate token
            tokens = Token.objects.filter(user=instance).all()
            tokens.delete()

            # if (instance.enterprise.permissions | validated_data['permissions']) != instance.enterprise.permissions:
            #     raise ValidationError('유효하지 않은 permission 입니다. 기업의 권한을 넘을 수 없습니다.')

            user_data = validated_data['permissions']
            enterprise_data = instance.enterprise.permissions

            num = 0
            for i in range(0, len(enterprise_data)):
                if (int(enterprise_data[i]) < int(user_data[i])):
                    raise ValidationError('유효하지 않은 permission 입니다. 기업의 권한을 넘을 수 없습니다.')
                    break

                num = num + 1

        user = super().update(instance, validated_data)
        if 'password' in validated_data:
            user.set_password(validated_data['password'])
            user.save()

        return user

    def validate_factory_classification(self, value):
        return self.code_validator(value, 104)

    def validate_employment_division(self, value):
        return self.code_validator(value, 112)

    def validate_job_position(self, value):
        return self.code_validator(value, 114)

    def validate_department_position(self, value):
        return self.code_validator(value, 113)

    def code_validator(self, code_master, group_code):
        if code_master is None:
            return code_master

        qs = GroupCodeMaster.objects.filter(pk=code_master.group_id, code=group_code)
        if qs.exists() is not True:
            message = '잘못된 코드 code must be a multiple of %d.' % group_code
            raise serializers.ValidationError(message)

        return code_master

    def to_internal_value(self, data):
        if type(data) is not dict:
            data._mutable = True

        if 'enterprise' not in data and self.context['view'].action == 'create':
            enterprise = self.context['request'].user.enterprise
            data['enterprise'] = enterprise.id

        return super(UserMasterSerializer, self).to_internal_value(data)

    def to_representation(self, instance):
        self.fields['factory_classification'] = CodeMasterSerializer()
        self.fields['employment_division'] = CodeMasterSerializer()
        self.fields['job_position'] = CodeMasterSerializer()
        self.fields['department_position'] = CodeMasterSerializer()


        return super(UserMasterSerializer, self).to_representation(instance)


class UserMasterSelectSerializer(serializers.ModelSerializer):
    code = serializers.CharField(max_length=8, required=False, read_only=True)
    created_by = serializers.CharField(required=False, read_only=True)  # 최종작성일
    created_at = serializers.CharField(required=False, read_only=True)  # 최초작성일
    enterprise_name = serializers.SerializerMethodField(read_only=True, required=False)

    class Meta:
        model = UserMaster
        fields = '__all__'
        optional_fields = ['enterprise']

    def get_enterprise_name(self, obj):
        if obj.enterprise:
            return obj.enterprise.name
        else:
            return "Seoul-soft"

    def get_at_date(self):
        return date.today()

    def get_by_username(self):
        return self.context['request'].user

    def get_code(self, obj):
        if obj['is_master'] is True:
            return obj['enterprise'].code + "0000"

        # print(obj['factory_classification'].id)
        # factory = str(obj['factory_classification'].id)[0]
        # division = str(obj['department_position'].id)[0]
        date = str(obj['employment_date']).replace('-', '')[2:6]
        order = '00'

        # prefix = factory + division + date
        prefix = 'UN' + date
        res = UserMaster.objects.filter(code__istartswith=prefix)
        if res.exists():
            num = res.order_by('-code').first().code[-2:]
            order = str(int(num) + 1)
            if len(order) == 1:
                order = '0' + order

        return 'UN' + date + order

    def create(self, instance):
        instance['code'] = self.get_code(instance)
        instance['created_at'] = self.get_at_date()
        instance['created_by'] = self.get_by_username()

        # is_master
        if instance['is_master'] is False:
            # if None in (instance['username']):
            #     raise ValidationError('유저이름은 필수 항목들입니다.')

            instance['enterprise'] = self.context['request'].user.enterprise
        else:
            instance['permissions'] = instance['enterprise'].permissions
            # 마스터 계정 생성 에러 관련
            instance['username'] = instance['enterprise'].name + ' 관리자'

        try:
            user = super().create(instance)
            user.set_password(instance['password'])
            user.save()
            return user
        except IntegrityError:
            raise ValidationError('유효하지 않은 code 이므로 생성할 수 없습니다.')  # TODO: Error message

    def update(self, instance, validated_data):

        if 'permissions' in validated_data:
            # invalidate token
            tokens = Token.objects.filter(user=instance).all()
            tokens.delete()

            # if (instance.enterprise.permissions | validated_data['permissions']) != instance.enterprise.permissions:
            #     raise ValidationError('유효하지 않은 permission 입니다. 기업의 권한을 넘을 수 없습니다.')

            user_data = validated_data['permissions']
            enterprise_data = instance.enterprise.permissions

            num = 0
            for i in range(0, len(enterprise_data)):
                if (int(enterprise_data[i]) < int(user_data[i])):
                    raise ValidationError('유효하지 않은 permission 입니다. 기업의 권한을 넘을 수 없습니다.')
                    break

                num = num + 1

        user = super().update(instance, validated_data)
        if 'password' in validated_data:
            user.set_password(validated_data['password'])
            user.save()

        return user

    def validate_factory_classification(self, value):
        return self.code_validator(value, 104)

    def validate_employment_division(self, value):
        return self.code_validator(value, 112)

    def validate_job_position(self, value):
        return self.code_validator(value, 114)

    def validate_department_position(self, value):
        return self.code_validator(value, 113)

    def code_validator(self, code_master, group_code):
        if code_master is None:
            return code_master

        qs = GroupCodeMaster.objects.filter(pk=code_master.group_id, code=group_code)
        if qs.exists() is not True:
            message = '잘못된 코드 code must be a multiple of %d.' % group_code
            raise serializers.ValidationError(message)

        return code_master

    def to_internal_value(self, data):
        if type(data) is not dict:
            data._mutable = True

        if 'enterprise' not in data and self.context['view'].action == 'create':
            enterprise = self.context['request'].user.enterprise
            data['enterprise'] = enterprise.id

        return super(UserMasterSelectSerializer, self).to_internal_value(data)

    def to_representation(self, instance):
        self.fields['factory_classification'] = CodeMasterSerializer()
        self.fields['employment_division'] = CodeMasterSerializer()
        self.fields['job_position'] = CodeMasterSerializer()
        self.fields['department_position'] = CodeMasterSerializer()


        return super(UserMasterSelectSerializer, self).to_representation(instance)


def custom_from_to_date(data):
    log_from = data.get('log_from', '1970-01-01')
    log_to = data.get('log_to', '9999-12-31')
    log_from = '1970-01-01' if log_from == '' else log_from
    log_to = '9999-12-31' if log_to == '' else log_to
    return log_from, log_to

