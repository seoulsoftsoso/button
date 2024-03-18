from datetime import datetime

from django.contrib.sessions.backends import file
from django.db import transaction
from django.http import JsonResponse
from django.shortcuts import render
from django.views import View

from api.base.base_form import group_code_fm
from api.models import UserMaster, CodeMaster, GroupCodeMaster
from lib import Pagenation
from msgs import msg_create_fail, msg_error, msg_pk, msg_delete_fail, msg_update_fail


class CodeMaster_in(View):
    def get(self, request, *args, **kwargs):
        context = {}
        context['gc'] = group_code_fm(request.GET, request.COOKIES['enterprise_name'])
        return render(request, 'basic_information/codemaster.html', context)


class CodeMaster_create(View):

    @transaction.atomic
    def post(self, request, *args, **kwargs):

        user_id = request.COOKIES['user_id']
        user = UserMaster.objects.get(id=user_id)

        code = request.POST.get('code', '')
        name = request.POST.get('name', '')
        explain = request.POST.get('explain', '')
        enable = request.POST.get('enable', '')

        if enable == 'true':
            enable = 1
        elif enable == 'false':
            enable = 0

        etc = request.POST.get('etc', '')

        group = request.POST.get('group', '')
        if group == '':
            group = None
        else:
            group = int(group)

        context = {}

        # 오늘날짜
        d_today = datetime.today().strftime('%Y-%m-%d')

        try:
            obj = CodeMaster.objects.create(

                code=code,
                name=name,
                explain=explain,
                enable=enable,
                etc=etc,
                group_id=group,

                created_by=user,
                updated_by=user,
                created_at=d_today,
                updated_at=d_today,
                enterprise=user.enterprise,
            )

            if obj:
                context = get_res(context, obj)
            else:
                msg = msg_create_fail
                return JsonResponse({'error': True, 'message': msg})

        except Exception as e:
            print('이게 발생했다고?')
            print(e)
            msg = msg_error
            for i in e.args:
                if i == 1062:
                    # msg = msg_1062
                    msg = '중복된 상세코드가 존재합니다.'

            return JsonResponse({'error': True, 'message': msg})

        return JsonResponse(context)


class CodeMaster_read(View):
    def get(self, request, *args, **kwargs):
        _page = request.GET.get('page', '1')
        _size = request.GET.get('page_size', '1')

        # 검색인자 - 그룹코드
        gc_name_sch = request.GET.get('gc_name_sch', '')

        qs = CodeMaster.objects.filter(enterprise__name=request.COOKIES['enterprise_name']) \
            .order_by('group__code', 'code')

        # Search
        if gc_name_sch != '':
            sc = GroupCodeMaster.objects.get(id=gc_name_sch)
            if sc:
                qs = qs.filter(group_id=sc.id)

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


class CodeMaster_update(View):

    @transaction.atomic
    def post(self, request):
        user_id = request.COOKIES['user_id']
        user = UserMaster.objects.get(id=user_id)

        pk = request.POST.get('pk')

        code = request.POST.get('code', '')
        name = request.POST.get('name', '')
        explain = request.POST.get('explain', '')
        enable = request.POST.get('enable', '')

        if enable == 'true':
            enable = 1
        elif enable == 'false':
            enable = 0

        etc = request.POST.get('etc', '')

        group = request.POST.get('group', '')
        if group == '':
            group = None
        else:
            group = int(group)

        context = {}

        # 오늘날짜
        d_today = datetime.today().strftime('%Y-%m-%d')

        try:
            obj = CodeMaster.objects.get(pk=int(pk))

            obj.code = code
            obj.name = name
            obj.explain = explain
            obj.enable = enable
            obj.etc = etc
            obj.group_id = group

            obj.updated_at = d_today
            obj.updated_by = user
            obj.enterprise = user.enterprise

            obj.save()

            if obj:
                context = get_res(context, obj)
            else:
                msg = msg_update_fail
                return JsonResponse({'error': True, 'message': msg})

        except Exception as e:
            print(e)

            msg = msg_error
            for i in e.args:
                if i == 1062:
                    # msg = msg_1062
                    msg = '중복된 상세코드가 존재합니다.'
                    break

            return JsonResponse({'error': True, 'message': msg})

        return JsonResponse(context)


class CodeMaster_delete(View):

    @transaction.atomic
    def post(self, request):

        pk = request.POST.get('pk', '')

        if (pk == ''):
            msg = msg_pk
            return JsonResponse({'error': True, 'message': msg})

        try:
            inv = CodeMaster.objects.get(pk=int(pk))
            inv.delete()
        except Exception as e:
            print('삭제 실패')
            print(e)
            # msg = msg_delete_fail
            msg = ["사용중인 데이터 입니다. 관련 데이터 삭제 후 다시 시도해주세요."]
            return JsonResponse({'error': True, 'message': msg})

        context = {}
        context['id'] = pk
        return JsonResponse(context)


def get_res(context, obj):
    context['id'] = obj.id
    context['code'] = obj.code
    context['name'] = obj.name
    context['explain'] = obj.explain
    context['enable'] = obj.enable
    context['etc'] = obj.etc

    if (obj.group):
        context['group_id'] = obj.group.id
        context['group_name'] = obj.group.name
    else:
        context['group_id'] = ''
        context['group_name'] = ''

    context['created_at'] = obj.created_at
    context['updated_at'] = obj.updated_at
    context['created_by_id'] = obj.created_by.id
    context['enterprise_id'] = obj.enterprise.id
    context['updated_by_id'] = obj.updated_by.id

    return context


def get_results(qs):
    results = []
    appendResult = results.append

    # id, 코드, 코드명, 설명, 사용유무, 등록자, 등록일, 최종수정자, 최종 변경일, 기타
    # 그룹코드의 코드, 코드명

    for row in qs.object_list:
        if (row.explain):
            explain = row.explain
        else:
            explain = ''

        if (row.etc):
            etc = row.etc
        else:
            etc = ''

        if (row.enable):
            enable = '사용'
        else:
            enable = '미사용'

        appendResult({
            'id': row.id,

            'code': row.code,
            'name': row.name,
            'enable': enable,

            'group_id': row.group.id,

            'group_code': row.group.code,
            'group_name': row.group.name,

            'explain': explain,
            'etc': row.etc,

            'created_by': row.created_by.username,
            'created_at': row.created_at,

            'updated_by': row.updated_by.username,
            'updated_at': row.updated_at,
        })

    return results
