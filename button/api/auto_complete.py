from django.db.models import Q, F
from django.db.models.functions import Coalesce

from api.models import GroupCodeMaster, CodeMaster, UserMaster, EnterpriseMaster
from dal import autocomplete


# 공장구분 104
class Code_104_ac(autocomplete.Select2QuerySetView):

    def get_queryset(self):
        qs = CodeMaster.objects.filter(
            enterprise__name=self.request.COOKIES['enterprise_name'], group__code=104, enable=True,
        ).order_by('name')

        if self.q:
            qs = qs.filter(name__contains=self.q).order_by('-id')

        return qs

    def get_result_label(self, item):
        return item.name


# 단위
class Code_105_ac(autocomplete.Select2QuerySetView):

    def get_queryset(self):
        qs = CodeMaster.objects.filter(
            enterprise__name=self.request.COOKIES['enterprise_name'], group__code=105, enable=True,
        )

        if self.q:
            qs = qs.filter(name__contains=self.q).order_by('-id')

        return qs

    def get_result_label(self, item):
        return item.name


# 용기타입 106
class Code_106_ac(autocomplete.Select2QuerySetView):

    def get_queryset(self):
        qs = CodeMaster.objects.filter(
            enterprise__name=self.request.COOKIES['enterprise_name'], group__code=106, enable=True,
        )

        if self.q:
            qs = qs.filter(name__contains=self.q).order_by('-id')

        return qs

    def get_result_label(self, item):
        return item.name


# 용기타입 106
class Code_107_ac(autocomplete.Select2QuerySetView):

    def get_queryset(self):
        qs = CodeMaster.objects.filter(
            enterprise__name=self.request.COOKIES['enterprise_name'], group__code=107, enable=True,
        )

        if self.q:
            qs = qs.filter(name__contains=self.q).order_by('-id')

        return qs

    def get_result_label(self, item):
        return item.name


# 거래구분 108
class Code_108_ac(autocomplete.Select2QuerySetView):

    def get_queryset(self):
        qs = CodeMaster.objects.filter(
            enterprise__name=self.request.COOKIES['enterprise_name'], group__code=108, enable=True,
        ).order_by('name')

        if self.q:
            qs = qs.filter(name__contains=self.q).order_by('-id')

        return qs

    def get_result_label(self, item):
        return item.name


# 공정구분 109
class Code_109_ac(autocomplete.Select2QuerySetView):

    def get_queryset(self):
        qs = CodeMaster.objects.filter(
            enterprise__name=self.request.COOKIES['enterprise_name'], group__code=109, enable=True,
        ).order_by('name')

        if self.q:
            qs = qs.filter(name__contains=self.q).order_by('-id')

        return qs

    def get_result_label(self, item):
        return item.name


# 작업장 110
class Code_110_ac(autocomplete.Select2QuerySetView):

    def get_queryset(self):
        qs = CodeMaster.objects.filter(
            enterprise__name=self.request.COOKIES['enterprise_name'], group__code=110, enable=True,
        ).order_by('name')

        if self.q:
            qs = qs.filter(name__contains=self.q).order_by('-id')

        return qs

    def get_result_label(self, item):
        return item.name


# 설비구분 111
class Code_111_ac(autocomplete.Select2QuerySetView):

    def get_queryset(self):
        qs = CodeMaster.objects.filter(
            enterprise__name=self.request.COOKIES['enterprise_name'], group__code=111, enable=True,
        ).order_by('name')

        if self.q:
            qs = qs.filter(name__contains=self.q).order_by('-id')

        return qs

    def get_result_label(self, item):
        return item.name


# 고용구분 112
class Code_112_ac(autocomplete.Select2QuerySetView):

    def get_queryset(self):
        qs = CodeMaster.objects.filter(
            enterprise__name=self.request.COOKIES['enterprise_name'], group__code=112, enable=True,
        ).order_by('name')

        if self.q:
            qs = qs.filter(name__contains=self.q).order_by('-id')

        return qs

    def get_result_label(self, item):
        return item.name


# 부서구분 113
class Code_113_ac(autocomplete.Select2QuerySetView):

    def get_queryset(self):
        qs = CodeMaster.objects.filter(
            enterprise__name=self.request.COOKIES['enterprise_name'], group__code=113, enable=True,
        ).order_by('name')

        if self.q:
            qs = qs.filter(name__contains=self.q).order_by('-id')

        return qs

    def get_result_label(self, item):
        return item.name


# 직위 114
class Code_114_ac(autocomplete.Select2QuerySetView):

    def get_queryset(self):
        qs = CodeMaster.objects.filter(
            enterprise__name=self.request.COOKIES['enterprise_name'], group__code=114, enable=True,
        ).order_by('name')

        if self.q:
            qs = qs.filter(name__contains=self.q).order_by('-id')

        return qs

    def get_result_label(self, item):
        return item.name


# 품종구분 115
class Code_115_ac(autocomplete.Select2QuerySetView):

    def get_queryset(self):
        qs = CodeMaster.objects.filter(
            enterprise__name=self.request.COOKIES['enterprise_name'], group__code=115, enable=True,
        ).order_by('name')

        if self.q:
            qs = qs.filter(name__contains=self.q).order_by('-id')

        return qs

    def get_result_label(self, item):
        return item.name


# 모델 116
class Code_116_ac(autocomplete.Select2QuerySetView):

    def get_queryset(self):
        qs = CodeMaster.objects.filter(
            enterprise__name=self.request.COOKIES['enterprise_name'], group__code=116, enable=True,
        )

        if self.q:
            qs = qs.filter(name__contains=self.q).order_by('-id')

        return qs

    def get_result_label(self, item):
        return item.name


# 자재분류 118
class Code_118_ac(autocomplete.Select2QuerySetView):

    def get_queryset(self):
        qs = CodeMaster.objects.filter(
            enterprise__name=self.request.COOKIES['enterprise_name'], group__code=118, enable=True,
        )

        if self.q:
            qs = qs.filter(name__contains=self.q).order_by('-id')

        return qs

    def get_result_label(self, item):
        return item.name


# 칼라구분 119
class Code_119_ac(autocomplete.Select2QuerySetView):

    def get_queryset(self):
        qs = CodeMaster.objects.filter(
            enterprise__name=self.request.COOKIES['enterprise_name'], group__code=119, enable=True,
        )

        if self.q:
            qs = qs.filter(name__contains=self.q).order_by('-id')

        return qs

    def get_result_label(self, item):
        return item.name


# 유성 - 브랜드 127
class Code_127_ac(autocomplete.Select2QuerySetView):

    def get_queryset(self):
        qs = CodeMaster.objects.filter(
            enterprise__name=self.request.COOKIES['enterprise_name'], group__code=127, enable=True,
        )

        if self.q:
            qs = qs.filter(name__contains=self.q).order_by('-id')

        return qs

    def get_result_label(self, item):
        return item.name


# 유성 - 제품군 128
class Code_128_ac(autocomplete.Select2QuerySetView):

    def get_queryset(self):
        qs = CodeMaster.objects.filter(
            enterprise__name=self.request.COOKIES['enterprise_name'], group__code=128, enable=True,
        )

        if self.q:
            qs = qs.filter(name__contains=self.q).order_by('-id')

        return qs

    def get_result_label(self, item):
        return item.name


# 사번
class User_code_ac(autocomplete.Select2QuerySetView):

    def get_queryset(self):
        qs = UserMaster.objects.filter(
            enterprise__name=self.request.COOKIES['enterprise_name'],
        ).order_by('-id')

        if self.q:
            qs = qs.filter(code__contains=self.q)

        return qs

    def get_result_label(self, item):
        return item.code


# 사용자명
class User_name_ac(autocomplete.Select2QuerySetView):

    def get_queryset(self):
        qs = UserMaster.objects.filter(
            enterprise__name=self.request.COOKIES['enterprise_name'],
        ).order_by('-id')

        if self.q:
            qs = qs.filter(code__contains=self.q)

        return qs

    def get_result_label(self, item):
        return item.username


# 사번 or 사용자명
class User_code_or_name_ac(autocomplete.Select2QuerySetView):

    def get_queryset(self):
        qs = UserMaster.objects.filter(
            enterprise__name=self.request.COOKIES['enterprise_name'],
        ).order_by('-id')

        if self.q:
            qs = qs.filter(Q(code__contains=self.q) | Q(username__contains=self.q))

        return qs

    def get_result_label(self, item):
        return item.code + ' : ' + item.username



# 그룹코드 명
class Gc_name_ac(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = GroupCodeMaster.objects.filter(
            enterprise__name=self.request.COOKIES['enterprise_name'],
        ).order_by('code')

        # enterprise_manage = self.request.COOKIES['enterprise_manage']
        # if (enterprise_manage == '(주)온교육'):
        #     # qs = qs.filter(~Q(code='111'))  # 설비구분
        #     # qs = qs.filter(~Q(code='117'))  # 버전구분
        #     # qs = qs.filter(~Q(code='119'))  # 칼라구분
        #     # qs = qs.filter(~Q(code='123'))  # 관리구분
        #     # qs = qs.filter(~Q(code='900'))  # 입고현황
        #
        #     qs = qs.filter(Q(code='104') |  # 공장구분
        #                    Q(code='105') |  # 단위
        #                    Q(code='106') |  # 용기타입
        #                    Q(code='107') |  # 창고구분
        #                    Q(code='108') |  # 거래구분
        #                    Q(code='109') |  # 공정구분
        #                    Q(code='110') |  # 작업장구분
        #
        #                    Q(code='112') |  # 사용자 구분
        #                    Q(code='113') |  # 부서 구분
        #                    Q(code='114') |  # 직위 구분
        #                    Q(code='115') |  # 품종 구분
        #                    Q(code='116') |  # 모델 구분
        #                    Q(code='118') |  # 자재구분
        #                    Q(code='124')  # 현황구분
        #                    )

        # for row in qs:
        #     code = row.code

        if self.q:
            qs = qs.filter(name__contains=self.q)

        return qs

    def get_result_label(self, item):
        return str(item.code) + ' (' + item.name + ')'


# 회사 정보 조회
class enterprise_name_ac(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        is_super = self.request.COOKIES.get('is_superuser')
        if is_super == 'true':
            qs = EnterpriseMaster.objects.all()
        else:
            qs = EnterpriseMaster.objects.filter(id=self.request.COOKIES.get('enterprise_id'))

        if self.q:
            qs = qs.filter(name__contains=self.q)

        return qs

    def get_result_label(self, result):
        return result.name


# 사용자 리스트
class client_name_ac(autocomplete.Select2QuerySetView):

    def get_queryset(self):

        enterprise = self.request.GET['enterPrise_id']

        if enterprise:
            # qs = UserMaster.objects.filter(Q(is_superuser=True) | Q(is_master=True)
            #                               , enterprise_id=enterprise).order_by('-id')
            qs = UserMaster.objects.filter(enterprise_id=enterprise).order_by('id')
        else:
            qs = UserMaster.objects.filter(enterprise_id=self.request.COOKIES['enterprise_id']).order_by('id')

        if self.q:
            qs = qs.filter(user_name__contains=self.q)

        return qs

    def get_result_label(self, result):
        return result.username

