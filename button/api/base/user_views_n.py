from datetime import datetime

from django.db import transaction
from django.http import JsonResponse
from django.shortcuts import render
from django.views import View

from api.base.base_form import user_fm
from api.models import UserMaster, CodeMaster
from lib import Pagenation
from msgs import msg_create_fail, msg_error, msg_pk, msg_delete_fail, msg_update_fail


class UserMaster_in(View):
    def get(self, request, *args, **kwargs):
        context = {}
        context['us'] = user_fm(request.GET, request.COOKIES['enterprise_name'])
        return render(request, 'basic_information/user.html', {})


class UserMaster_create(View):

    @transaction.atomic
    def post(self, request):

        user_id = request.COOKIES['user_id']
        user = UserMaster.objects.get(id=user_id)


        code = int(request.POST.get('code', ''))
        name = request.POST.get('name', '')

        division = request.POST.get('division', '')
        if division == '':
            division = None
        else:
            division = int(division)

        licensee_number = request.POST.get('licensee_number', '')
        owner_name = request.POST.get('owner_name', '')
        business_conditions = request.POST.get('business_conditions', '')
        business_event = request.POST.get('business_event', '')
        postal_code = request.POST.get('postal_code', '')
        address = request.POST.get('address', '')
        office_phone = request.POST.get('office_phone', '')
        office_fax = request.POST.get('office_fax', '')
        charge_name = request.POST.get('charge_name', '')
        charge_level = request.POST.get('charge_level', '')
        charge_phone = request.POST.get('charge_phone', '')
        email = request.POST.get('email', '')
        etc = request.POST.get('etc', '')

        context = {}

        # 오늘날짜
        d_today = datetime.today().strftime('%Y-%m-%d')

        try:
            print()

        except Exception as e:

            msg = msg_error
            for i in e.args:
                if i == 1062:
                    # msg = msg_1062
                    msg = '중복된 거래처가 존재합니다.'

            return JsonResponse({'error': True, 'message': msg})

        return JsonResponse(context)


class UserMaster_read(View):
    def get(self, request, *args, **kwargs):
        _page = request.GET.get('page', '1')
        _size = request.GET.get('page_size', '10')

        # 검색인자 1.공장구분, 2.부서구분, 3.사용자명
        us_factory_sch = request.GET.get('us_factory_sch', '')
        us_depart_sch = request.GET.get('us_depart_sch', '')
        us_name_sch = request.GET.get('us_name_sch', '')

        is_superuser = request.COOKIES['is_superuser']

        if is_superuser == 'true':
            qs = UserMaster.objects.all().order_by('-id')
        else:
            qs = UserMaster.objects.filter(enterprise__name=request.COOKIES['enterprise_name']).order_by('-id')

        # Search
        if us_factory_sch != '':
            sc = CodeMaster.objects.get(id=us_factory_sch)
            if sc:
                qs = qs.filter(factory_classification_id=sc.id)

        if us_depart_sch != '':
            sc = CodeMaster.objects.get(id=us_depart_sch)
            if sc:
                qs = qs.filter(department_position_id=sc.id)

        if us_name_sch != '':
            qs = qs.filter(username__contains=us_name_sch)

        # Pagination
        qs_ps = Pagenation(qs, _size, _page)

        pre = int(_page) - 1
        url_pre = "/?page_size=" + _size + "&page=" + str(pre)
        if pre < 1:
            url_pre = None

        next = int(_page) + 1
        url_next = "/?page_size=" + _size + "&page=" + str(next)
        if next > qs_ps.paginator.num_pages:
            url_next = None

        results = get_results(qs_ps)

        context = {}
        context['count'] = qs_ps.paginator.count
        context['previous'] = url_pre
        context['next'] = url_next
        context['results'] = results

        return JsonResponse(context, safe=False)


class UserMaster_update(View):

    @transaction.atomic
    def post(self, request):
        user_id = request.COOKIES['user_id']
        user = UserMaster.objects.get(id=user_id)
        # enterprise = request.COOKIES['enterprise_id']

        pk = request.POST.get('pk', '')
        if (pk == ''):
            msg = msg_pk
            return JsonResponse({'error': True, 'message': msg})

        code = int(request.POST.get('code', ''))
        name = request.POST.get('name', '')

        division = request.POST.get('division', '')
        if division == '':
            division = None
        else:
            division = int(division)

        licensee_number = request.POST.get('licensee_number', '')
        owner_name = request.POST.get('owner_name', '')
        business_conditions = request.POST.get('business_conditions', '')
        business_event = request.POST.get('business_event', '')
        postal_code = request.POST.get('postal_code', '')
        address = request.POST.get('address', '')
        office_phone = request.POST.get('office_phone', '')
        office_fax = request.POST.get('office_fax', '')
        charge_name = request.POST.get('charge_name', '')
        charge_level = request.POST.get('charge_level', '')
        charge_phone = request.POST.get('charge_phone', '')
        email = request.POST.get('email', '')
        etc = request.POST.get('etc', '')

        context = {}

        # 오늘날짜
        d_today = datetime.today().strftime('%Y-%m-%d')

        try:

           print()

        except Exception as e:
            msg = msg_error
            for i in e.args:
                if i == 1062:
                    # msg = msg_1062
                    # 수정할 때는 발생하지 않는 에러일텐데? 일단 냅둠.
                    msg = '중복된 거래처가 존재합니다.'
                    break

            return JsonResponse({'error': True, 'message': msg})

        return JsonResponse(context)


class UserMaster_delete(View):

    @transaction.atomic
    def post(self, request):
        pk = request.POST.get('pk', '')
        if (pk == ''):
            msg = msg_pk
            return JsonResponse({'error': True, 'message': msg})



        context = {}
        context['id'] = pk
        return JsonResponse(context)


def get_res(context, obj):
    context['id'] = obj.id
    context['code'] = obj.code
    context['name'] = obj.name
    context['licensee_number'] = obj.licensee_number

    context['business_conditions'] = obj.business_conditions
    context['business_event'] = obj.business_event
    context['postal_code'] = obj.postal_code
    context['address'] = obj.address
    context['office_phone'] = obj.office_phone
    context['office_fax'] = obj.office_fax
    context['charge_name'] = obj.charge_name
    context['charge_phone'] = obj.charge_phone
    context['charge_level'] = obj.charge_level
    context['email'] = obj.email
    context['enable'] = obj.enable
    context['etc'] = obj.etc
    context['created_at'] = obj.created_at
    context['updated_at'] = obj.updated_at
    context['created_by_id'] = obj.created_by.id
    context['enterprise_id'] = obj.enterprise.id
    context['updated_by_id'] = obj.updated_by.id

    if (obj.division):
        context['division_id'] = obj.division.id
        context['division_name'] = obj.division.name
    else:
        context['division_id'] = ''
        context['division_name'] = ''

    return context


def get_results(qs):
    results = []
    appendResult = results.append

    for row in qs.object_list:
        # 입사일자, 우편번호, 주소, 전화번호, email, 기타
        if (row.employment_date):
            employment_date = row.employment_date
        else:
            employment_date = ''

        if (row.postal_code):
            postal_code = row.postal_code
        else:
            postal_code = ''

        if (row.address):
            address = row.address
        else:
            address = ''

        if (row.etc):
            etc = row.etc
        else:
            etc = ''

        if (row.email):
            email = row.email
        else:
            email = ''

        if (row.tel):
            tel = row.tel
        else:
            tel = ''

        # 부서구분, 고용구분, 공장구분, 직위구분, 거래처
        if (row.department_position_id):
            department_position_id = row.department_position.id
            department_position_name = row.department_position.name
        else:
            department_position_id = ''
            department_position_name = ''

        if (row.employment_division_id):
            employment_division_id = row.employment_division.id
            employment_division_name = row.employment_division.name
        else:
            employment_division_id = ''
            employment_division_name = ''

        if (row.factory_classification_id):
            factory_classification_id = row.factory_classification.id
            factory_classification_name = row.factory_classification.name
        else:
            factory_classification_id = ''
            factory_classification_name = ''

        if (row.job_position_id):
            job_position_id = row.job_position.id
            job_position_name = row.job_position.name
        else:
            job_position_id = ''
            job_position_name = ''

        if (row.order_company_id):
            order_company_id = row.order_company.id
            order_company_name = row.order_company.name
        else:
            order_company_id = ''
            order_company_name = ''

        appendResult({
            # 사번, 사용자명, id, 비밀번호 필수
            'code': row.code,
            'username': row.username,
            'user_id': row.user_id,
            'password': row.password,

            'created_at': row.created_at,
            'created_by': row.created_by_id,

            'employment_date': employment_date,
            'postal_code': postal_code,
            'address': address,
            'etc': etc,
            'email': email,
            'tel': tel,

            # enterprise_id 생략

            'department_position_id': department_position_id,
            'department_position_name': department_position_name,

            'employment_division_id': employment_division_id,
            'employment_division_name': employment_division_name,

            'factory_classification_id': factory_classification_id,
            'factory_classification_name': factory_classification_name,

            'job_position_id': job_position_id,
            'job_position_name': job_position_name,

            'order_company_id': order_company_id,
            'order_company_name': order_company_name,
        })

    return results
