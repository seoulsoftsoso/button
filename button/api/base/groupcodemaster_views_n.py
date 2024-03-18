from datetime import datetime

from django.db import transaction
from django.http import JsonResponse
from django.shortcuts import render
from django.views import View

from api.models import UserMaster, CodeMaster, GroupCodeMaster
from lib import Pagenation
from msgs import msg_create_fail, msg_error, msg_update_fail


class GroupCode_in(View):
    def get(self, request, *args, **kwargs):
        context = {}
        # context['gc'] = group_code_fm(request.GET, request.COOKIES['enterprise_name'])
        return render(request, 'basic_information/codemaster_managepopup.html', context)


class GroupCode_create(View):
    @transaction.atomic
    def post(self, request, *args, **kwargs):
        user_id = request.COOKIES['user_id']
        user = UserMaster.objects.get(id=user_id)

        d_today = datetime.today().strftime('%Y-%m-%d')

        list_codemaster = []
        list_codemaster.append({'code': 104, 'name': '공장구분'})
        list_codemaster.append({'code': 105, 'name': '단위'})
        list_codemaster.append({'code': 106, 'name': '용기타입'})
        list_codemaster.append({'code': 107, 'name': '창고구분'})
        list_codemaster.append({'code': 108, 'name': '거래구분'})
        list_codemaster.append({'code': 109, 'name': '공정구분(세부공정)'})
        list_codemaster.append({'code': 110, 'name': '작업장구분'})
        list_codemaster.append({'code': 111, 'name': '설비구분'})
        list_codemaster.append({'code': 112, 'name': '사용자(고용)구분'})
        list_codemaster.append({'code': 113, 'name': '부서구분'})
        list_codemaster.append({'code': 114, 'name': '직위(직급)구분'})
        list_codemaster.append({'code': 115, 'name': '품종(품목)구분'})
        list_codemaster.append({'code': 116, 'name': '모델'})
        list_codemaster.append({'code': 117, 'name': '버전구분'})
        list_codemaster.append({'code': 118, 'name': '자재분류(품목구분)'})
        list_codemaster.append({'code': 119, 'name': '칼라구분'})
        list_codemaster.append({'code': 122, 'name': '대여품구분'})
        list_codemaster.append({'code': 123, 'name': '온습도관리구분'})
        list_codemaster.append({'code': 124, 'name': '현황(작업진행현황)구분'})
        list_codemaster.append({'code': 125, 'name': '불량사유 대분류'})
        list_codemaster.append({'code': 126, 'name': '불량사유 소분류'})
        list_codemaster.append({'code': 127, 'name': '브랜드'})
        list_codemaster.append({'code': 128, 'name': '제품군'})
        list_codemaster.append({'code': 900, 'name': '입고현황'})

        context = {}

        qs = GroupCodeMaster.objects.filter(enterprise=request.COOKIES['enterprise_id'])

        try:
            for a in range(0, len(list_codemaster)):
                # 이름이 수정되었을 수도 있으므로, 코드만 비교

                if qs.filter(code=list_codemaster[a]['code']).count() == 0:
                    # 생성
                    GroupCodeMaster.objects.create(
                        code=list_codemaster[a]['code'], name=list_codemaster[a]['name'],
                        enable=True, created_at=d_today, updated_at=d_today,
                        created_by=user, enterprise=user.enterprise, updated_by=user
                    )

        except Exception as e:
            print('이게 발생했다고?')
            print(e)
            msg = "그룹코드 기본값 생성중에 에러가 발생했습니다."
            # for i in e.args:
            #     if i == 1062:
            #         # msg = msg_1062
            #         msg = '중복된 그룹코드가 존재합니다.'
            #         print('문제5')
            #
            # return JsonResponse({'error': True, 'message': msg})

        return JsonResponse(context)


class GroupCode_read(View):
    def get(self, request, *args, **kwargs):
        _page = request.GET.get('page', '1')
        # 한 화면에 보여줄 리스트 개수
        _size = request.GET.get('page_size', '20')

        qs = GroupCodeMaster.objects.filter(enterprise__name=request.COOKIES['enterprise_name']) \
            .order_by('code')

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


class GroupCode_update(View):

    @transaction.atomic
    def post(self, request):
        user_id = request.COOKIES['user_id']
        user = UserMaster.objects.get(id=user_id)

        pk = request.POST.get('pk')

        code = request.POST.get('code', '')
        name = request.POST.get('name', '')

        context = {}

        # 오늘날짜
        d_today = datetime.today().strftime('%Y-%m-%d')

        try:
            obj = GroupCodeMaster.objects.get(pk=int(pk))

            obj.code = code
            obj.name = name

            obj.updated_at = d_today
            obj.updated_by = user
            # obj.enterprise = user.enterprise

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
                    msg = '중복된 그룹코드가 존재합니다.'
                    break

            return JsonResponse({'error': True, 'message': msg})

        return JsonResponse(context)


def get_res(context, obj):
    context['id'] = obj.id
    context['code'] = obj.code
    context['name'] = obj.name

    context['created_at'] = obj.created_at
    context['updated_at'] = obj.updated_at
    context['created_by_id'] = obj.created_by.id
    # context['enterprise_id'] = obj.enterprise.id
    context['updated_by_id'] = obj.updated_by.id

    return context


def get_results(qs):
    results = []
    appendResult = results.append

    # id, 코드, 코드명, 사용유무, 등록자, 등록일, 최종수정자, 최종 변경일

    for row in qs.object_list:
        appendResult({
            'id': row.id,

            'code': row.code,
            'name': row.name,
            'enable': row.enable,

            'created_by': row.created_by.username,
            'created_at': row.created_at,

            'updated_by': row.updated_by.username,
            'updated_at': row.updated_at,
        })

    return results
