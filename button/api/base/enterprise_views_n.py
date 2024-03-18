from datetime import datetime

from django.db import transaction
from django.http import JsonResponse
from django.shortcuts import render
from django.views import View

from api.models import UserMaster, CodeMaster, EnterpriseMaster
from lib import Pagenation
from msgs import msg_create_fail, msg_error, msg_pk, msg_delete_fail, msg_update_fail


class EnterpriseMaster_in(View):
    def get(self, request, *args, **kwargs):
        context = {}
        # context['it'] = item_fm(request.GET, request.COOKIES['enterprise_name'])
        return render(request, 'basic_information/new_enterprise_register.html', context)


class EnterpriseMaster_create(View):

    @transaction.atomic
    def post(self, request, *args, **kwargs):

        code = request.POST.get('code', '')
        name = request.POST.get('name', '')
        manage = request.POST.get('manage', '')
        permissions = request.POST.get('permissions')

        context = {}

        try:
            obj = EnterpriseMaster.objects.create(
                code=code,
                name=name,
                manage=manage,
                permissions=permissions,
            )

            if obj:
                context = get_res(context, obj)
            else:
                msg = msg_create_fail
                return JsonResponse({'error': True, 'message': msg})

        except Exception as e:
            print(e)

            msg = msg_error
            for i in e.args:
                if i == 1062:
                    # msg = msg_1062
                    msg = '중복된 기업코드가 존재합니다.'

            return JsonResponse({'error': True, 'message': msg})

        return JsonResponse(context)


class EnterpriseMaster_read(View):
    def get(self, request, *args, **kwargs):
        _page = request.GET.get('page', '1')
        _size = request.GET.get('page_size', '1')

        # 검색인자 - 품번, 품명, 자재분류

        qs = EnterpriseMaster.objects.all().order_by('code')

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


class EnterpriseMaster_update(View):

    @transaction.atomic
    def post(self, request):

        pk = request.POST.get('pk', '')
        if (pk == ''):
            msg = msg_pk
            return JsonResponse({'error': True, 'message': msg})

        code = request.POST.get('code', '')
        name = request.POST.get('name', '')
        manage = request.POST.get('manage', '')

        context = {}

        try:
            obj = EnterpriseMaster.objects.get(pk=int(pk))

            obj.code = code
            obj.name = name
            obj.manage = manage

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
                    msg = '중복된 기업코드가 존재합니다.'
                    break

            return JsonResponse({'error': True, 'message': msg})

        return JsonResponse(context)


class EnterpriseMaster_delete(View):

    @transaction.atomic
    def post(self, request):

        pk = request.POST.get('pk', '')

        if (pk == ''):
            msg = msg_pk
            return JsonResponse({'error': True, 'message': msg})

        try:
            inv = EnterpriseMaster.objects.get(pk=int(pk))
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
    context['manage'] = obj.manage

    context['permissions'] = obj.permissions

    return context


def get_results(qs):
    results = []
    appendResult = results.append

    # id, 코드, 기업명, 관리명

    for row in qs.object_list:
        appendResult({
            'id': row.id,
            'code': row.code,
            'name': row.name,
            'manage': row.manage,
        })

    return results
