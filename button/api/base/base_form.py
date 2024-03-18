from dal import autocomplete
from django import forms

from api.models import GroupCodeMaster, CodeMaster, EnterpriseMaster, UserMaster


# 코드 마스터
class group_code_fm(forms.Form):

    def __init__(self, *args, **kwargs):
        super(group_code_fm, self).__init__(*args, **kwargs)
        self.enterpriseName = args[1]

    enterpriseName = '서울소프트'
    qs_group_code = GroupCodeMaster.objects.none()

    gc_name_sch = forms.ModelChoiceField(required=False,
                                         queryset=qs_group_code,
                                         widget=autocomplete.ListSelect2(
                                             url='gc_name_ac',
                                             attrs={
                                                 'class': 'form-control form-control-sm',
                                                 'style': 'width:100%; height:100%',
                                                 'data-placeholder': '선택 및 검색',
                                             }),
                                         )

    gc_name_add = forms.ModelChoiceField(required=False,
                                         queryset=qs_group_code,
                                         widget=autocomplete.ListSelect2(
                                             url='gc_name_ac',
                                             attrs={
                                                 'class': 'form-control form-control-sm',
                                                 'style': 'width:100%; height:100%',
                                                 'data-placeholder': '선택 및 검색',
                                             }),
                                         )


# 거래처 기준정보관리
class customer_fm(forms.Form):

    def __init__(self, *args, **kwargs):
        super(customer_fm, self).__init__(*args, **kwargs)
        self.enterpriseName = args[1]

    enterpriseName = '서울소프트'

    qs_code_master = CodeMaster.objects.none()

    # Search
    # 거래구분 code108_name_ac
    cu_division_sch = forms.ModelChoiceField(required=False,
                                             queryset=qs_code_master,
                                             widget=autocomplete.ListSelect2(
                                                 url='code108_name_ac',
                                                 attrs={
                                                     'class': 'form-control form-control-sm',
                                                     'style': 'width:100%; height:100%',
                                                     'data-placeholder': '선택 및 검색',
                                                 }),
                                             )

    # 거래처 명 customer_name_ac
    cu_name_sch = forms.ModelChoiceField(required=False,
                                         queryset=qs_code_master,
                                         widget=autocomplete.ListSelect2(
                                             url='customer_name_ac',
                                             attrs={
                                                 'class': 'form-control form-control-sm',
                                                 'style': 'width:100%; height:100%',
                                                 'data-placeholder': '선택 및 검색',
                                             }),
                                         )

    # 거래처 명 form에서 사용
    cu_name_form = forms.ModelChoiceField(required=False,
                                          queryset=qs_code_master,
                                          widget=autocomplete.ListSelect2(
                                              url='customer_name_ac',
                                              attrs={
                                                  'class': 'form-control form-control-sm',
                                                  'style': 'width:100%; height:100%',
                                                  'data-placeholder': '선택 및 검색',
                                              }),
                                          )

    # Add
    # 거래구분 code108_name_ac
    cu_division_add = forms.ModelChoiceField(required=False,
                                             queryset=qs_code_master,
                                             widget=autocomplete.ListSelect2(
                                                 url='code108_name_ac',
                                                 attrs={
                                                     'class': 'form-control form-control-sm',
                                                     'style': 'width:100%; height:100%',
                                                     'data-placeholder': '선택 및 검색',
                                                 }),
                                             )


# 사용자 기준정보관리
class user_fm(forms.Form):

    def __init__(self, *args, **kwargs):
        super(user_fm, self).__init__(*args, **kwargs)
        self.enterpriseName = args[1]

    enterpriseName = '서울소프트'
    qs_code_master = CodeMaster.objects.none()

    us_factory_sch = forms.ModelChoiceField(required=False,
                                            queryset=qs_code_master,
                                            widget=autocomplete.ListSelect2(
                                                url='code104_name_ac',
                                                attrs={
                                                    'class': 'form-control form-control-sm h-100 w-100',
                                                    'data-placeholder': '선택 및 검색',
                                                }),
                                            )

    us_depart_sch = forms.ModelChoiceField(required=False,
                                           queryset=qs_code_master,
                                           widget=autocomplete.ListSelect2(
                                               url='code113_name_ac',
                                               attrs={
                                                   'class': 'form-control form-control-sm h-100 w-100',
                                                   'data-placeholder': '선택 및 검색',
                                               }),
                                           )

    us_factory_add = forms.ModelChoiceField(required=False,
                                            queryset=qs_code_master,
                                            widget=autocomplete.ListSelect2(
                                                url='code104_name_ac',
                                                attrs={
                                                    'class': 'form-control form-control-sm h-100 w-100',
                                                    'data-placeholder': '선택 및 검색',
                                                }),
                                            )

    us_depart_add = forms.ModelChoiceField(required=False,
                                           queryset=qs_code_master,
                                           widget=autocomplete.ListSelect2(
                                               url='code113_name_ac',
                                               attrs={
                                                   'class': 'form-control form-control-sm h-100 w-100',
                                                   'data-placeholder': '선택 및 검색',
                                               }),
                                           )

    # 고용구분 112
    us_emp_div_add = forms.ModelChoiceField(required=False,
                                            queryset=qs_code_master,
                                            widget=autocomplete.ListSelect2(
                                                url='code112_name_ac',
                                                attrs={
                                                    'class': 'form-control form-control-sm h-100 w-100',
                                                    'data-placeholder': '선택 및 검색',
                                                }),
                                            )

    # 직위 114
    us_job_pos_add = forms.ModelChoiceField(required=False,
                                            queryset=qs_code_master,
                                            widget=autocomplete.ListSelect2(
                                                url='code114_name_ac',
                                                attrs={
                                                    'class': 'form-control form-control-sm h-100 w-100',
                                                    'data-placeholder': '선택 및 검색',
                                                }),
                                            )


# 품목 기준정보관리
class item_fm(forms.Form):

    def __init__(self, *args, **kwargs):
        initial_values = kwargs.get('initial', {})
        initial_values.setdefault('it_location_add', '입고창고')
        kwargs['initial'] = initial_values
        super(item_fm, self).__init__(*args, **kwargs)
        self.enterpriseName = args[1]



    enterpriseName = '서울소프트'
    # qs_it = ItemMaster.objects.none()
    qs_cm = CodeMaster.objects.none()


    # search

    # 품번
    it_code_sch = forms.ModelChoiceField(required=False,
                                         queryset=qs_cm,
                                         widget=autocomplete.ListSelect2(
                                             url='item_code_ac',
                                             attrs={
                                                 'class': 'form-control form-control-sm',
                                                 'style': 'width:100%; height:100%',
                                                 'data-placeholder': '선택 및 검색',
                                             }),
                                         )
    # 거래처 명 customer_name_ac
    cu_name_sch = forms.ModelChoiceField(required=False,
                                         queryset=qs_cm,
                                         widget=autocomplete.ListSelect2(
                                             url='customer_name_ac',
                                             attrs={
                                                 'class': 'form-control form-control-sm',
                                                 'style': 'width:100%; height:100%',
                                                 'data-placeholder': '선택 및 검색',
                                             }),
                                         )

    # form에서 사용할 품번
    it_code_form = forms.ModelChoiceField(required=False,
                                          queryset=qs_cm,
                                          widget=autocomplete.ListSelect2(
                                              url='item_code_ac',
                                              attrs={
                                                  'class': 'form-control form-control-sm',
                                                  'style': 'width:100%; height:100%',
                                                  'data-placeholder': '선택 및 검색',
                                              }),
                                          )

    # 품명
    it_name_sch = forms.ModelChoiceField(required=False,
                                         queryset=qs_cm,
                                         widget=autocomplete.ListSelect2(
                                             url='item_name_ac',
                                             attrs={
                                                 'class': 'form-control form-control-sm',
                                                 'style': 'width:100%; height:100%',
                                                 'data-placeholder': '선택 및 검색',
                                             }),
                                         )

    # form에서 사용할 품명
    it_name_form = forms.ModelChoiceField(required=False,
                                          queryset=qs_cm,
                                          widget=autocomplete.ListSelect2(
                                              url='item_name_ac',
                                              attrs={
                                                  'class': 'form-control form-control-sm',
                                                  'style': 'width:100%; height:100%',
                                                  'data-placeholder': '선택 및 검색',
                                              }),
                                          )

    # 나이스번호
    it_nice_number_sch = forms.ModelChoiceField(required=False,
                                                queryset=qs_cm,
                                                widget=autocomplete.ListSelect2(
                                                    url='item_nice_number_ac',
                                                    attrs={
                                                        'class': 'form-control form-control-sm',
                                                        'style': 'width:100%; height:100%',
                                                        'data-placeholder': '선택 및 검색',
                                                    }),
                                                )

    # 자재분류 118 code118_name_ac
    it_division_sch = forms.ModelChoiceField(required=False,
                                             queryset=qs_cm,
                                             widget=autocomplete.ListSelect2(
                                                 url='code118_name_ac',
                                                 attrs={
                                                     'class': 'form-control form-control-sm',
                                                     'style': 'width:100%; height:100%',
                                                     'data-placeholder': '선택 및 검색',
                                                 }),
                                             )

    # add
    # 자재분류 118 code118_name_ac
    it_division_add = forms.ModelChoiceField(required=False,
                                             queryset=qs_cm,
                                             widget=autocomplete.ListSelect2(
                                                 url='code118_name_ac',
                                                 attrs={
                                                     'class': 'form-control form-control-sm',
                                                     'style': 'width:100%; height:100%',
                                                     'data-placeholder': '선택 및 검색',
                                                 }),
                                             )
    # 브랜드 127 code127_name_ac
    it_division_add = forms.ModelChoiceField(required=False,
                                             queryset=qs_cm,
                                             widget=autocomplete.ListSelect2(
                                                 url='code118_name_ac',
                                                 attrs={
                                                     'class': 'form-control form-control-sm',
                                                     'style': 'width:100%; height:100%',
                                                     'data-placeholder': '선택 및 검색',
                                                 }),
                                             )

    # 제품군 128 code128_name_ac
    it_brand = forms.ModelChoiceField(required=False,
                                      queryset=qs_cm,
                                      widget=autocomplete.ListSelect2(
                                          url='code127_name_ac',
                                          attrs={
                                              'class': 'form-control form-control-sm',
                                              'style': 'width:100%; height:100%',
                                              'data-placeholder': '선택 및 검색',
                                          }),
                                      )

    # 제품군 118 code118_name_ac
    it_item_group = forms.ModelChoiceField(required=False,
                                           queryset=qs_cm,
                                           widget=autocomplete.ListSelect2(
                                               url='code128_name_ac',
                                               attrs={
                                                   'class': 'form-control form-control-sm',
                                                   'style': 'width:100%; height:100%',
                                                   'data-placeholder': '선택 및 검색',
                                               }),
                                           )

    # 제품군 128 code128_name_ac
    it_brand_sch = forms.ModelChoiceField(required=False,
                                          queryset=qs_cm,
                                          widget=autocomplete.ListSelect2(
                                              url='code127_name_ac',
                                              attrs={
                                                  'class': 'form-control form-control-sm',
                                                  'style': 'width:100%; height:100%',
                                                  'data-placeholder': '선택 및 검색',
                                              }),
                                          )

    # 자재분류 118 code118_name_ac
    it_item_group_sch = forms.ModelChoiceField(required=False,
                                               queryset=qs_cm,
                                               widget=autocomplete.ListSelect2(
                                                   url='code128_name_ac',
                                                   attrs={
                                                       'class': 'form-control form-control-sm',
                                                       'style': 'width:100%; height:100%',
                                                       'data-placeholder': '선택 및 검색',
                                                   }),
                                               )

    # 모델 116 code116_name_ac
    it_model_add = forms.ModelChoiceField(required=False,
                                          queryset=qs_cm,
                                          widget=autocomplete.ListSelect2(
                                              url='code116_name_ac',
                                              attrs={
                                                  'class': 'form-control form-control-sm',
                                                  'style': 'width:100%; height:100%',
                                                  'data-placeholder': '선택 및 검색',
                                              }),
                                          )

    # 단위 105 code105_name_ac
    it_unit_add = forms.ModelChoiceField(required=False,
                                         queryset=qs_cm,
                                         widget=autocomplete.ListSelect2(
                                             url='code105_name_ac',
                                             attrs={
                                                 'class': 'form-control form-control-sm',
                                                 'style': 'width:100%; height:100%',
                                                 'data-placeholder': '선택 및 검색',
                                             }),
                                         )

    # 거래처
    it_customer_add = forms.ModelChoiceField(required=False,
                                             queryset=qs_cm,
                                             widget=autocomplete.ListSelect2(
                                                 url='customer_name_ac',
                                                 attrs={
                                                     'class': 'form-control form-control-sm',
                                                     'style': 'width:100%; height:100%',
                                                     'data-placeholder': '선택 및 검색',
                                                 }),
                                             )
    # 거래처
    it_customer_add_code = forms.ModelChoiceField(required=False,
                                                  queryset=qs_cm,
                                                  widget=autocomplete.ListSelect2(
                                                      url='customer_code_ac',
                                                      attrs={
                                                          'class': 'form-control form-control-sm',
                                                          'style': 'width:100%; height:100%',
                                                          'data-placeholder': '선택 및 검색',
                                                      }),
                                                  )

    # 거래처
    it_customer2_add = forms.ModelChoiceField(required=False,
                                              queryset=qs_cm,
                                              widget=autocomplete.ListSelect2(
                                                  url='customer_name_ac',
                                                  attrs={
                                                      'class': 'form-control form-control-sm',
                                                      'style': 'width:100%; height:100%',
                                                      'data-placeholder': '선택 및 검색',
                                                  }),
                                              )

    # 거래처
    it_customer2_add_code = forms.ModelChoiceField(required=False,
                                                   queryset=qs_cm,
                                                   widget=autocomplete.ListSelect2(
                                                       url='customer_code_ac',
                                                       attrs={
                                                           'class': 'form-control form-control-sm',
                                                           'style': 'width:100%; height:100%',
                                                           'data-placeholder': '선택 및 검색',
                                                       }),
                                                   )

    # 거래처
    it_customer3_add = forms.ModelChoiceField(required=False,
                                              queryset=qs_cm,
                                              widget=autocomplete.ListSelect2(
                                                  url='customer_name_ac',
                                                  attrs={
                                                      'class': 'form-control form-control-sm',
                                                      'style': 'width:100%; height:100%',
                                                      'data-placeholder': '선택 및 검색',
                                                  }),
                                              )
    # 거래처
    it_customer3_add_code = forms.ModelChoiceField(required=False,
                                                   queryset=qs_cm,
                                                   widget=autocomplete.ListSelect2(
                                                       url='customer_code_ac',
                                                       attrs={
                                                           'class': 'form-control form-control-sm',
                                                           'style': 'width:100%; height:100%',
                                                           'data-placeholder': '선택 및 검색',
                                                       }),
                                                   )
    # 용기타입 106 code106_name_ac
    it_container_add = forms.ModelChoiceField(required=False,
                                              queryset=qs_cm,
                                              widget=autocomplete.ListSelect2(
                                                  url='code106_name_ac',
                                                  attrs={
                                                      'class': 'form-control form-control-sm',
                                                      'style': 'width:100%; height:100%',
                                                      'data-placeholder': '선택 및 검색',
                                                  }),
                                              )

    # 칼라구분 119 code119_name_ac
    it_color_add = forms.ModelChoiceField(required=False,
                                          queryset=qs_cm,
                                          widget=autocomplete.ListSelect2(
                                              url='code119_name_ac',
                                              attrs={
                                                  'class': 'form-control form-control-sm',
                                                  'style': 'width:100%; height:100%',
                                                  'data-placeholder': '선택 및 검색',
                                              }),
                                          )

    # 품종구분 115 code115_name_ac
    it_kind_add = forms.ModelChoiceField(required=False,
                                         queryset=qs_cm,
                                         widget=autocomplete.ListSelect2(
                                             url='code115_name_ac',
                                             attrs={
                                                 'class': 'form-control form-control-sm',
                                                 'style': 'width:100%; height:100%',
                                                 'data-placeholder': '선택 및 검색',
                                             }),
                                         )

    # 창고구분 107 code107_name_ac
    it_location_add = forms.ModelChoiceField(required=False,
                                             queryset=qs_cm,
                                             widget=autocomplete.ListSelect2(
                                                 url='code107_name_ac',
                                                 attrs={
                                                     'class': 'form-control form-control-sm',
                                                     'style': 'width:100%; height:100%',
                                                     'data-placeholder': '선택 및 검색',
                                                 }),
                                             )

    # 수수료율 스마트름뱅이
    it_item_fee_rate = forms.ModelChoiceField(required=False,
                                              queryset=qs_cm,
                                              widget=autocomplete.ListSelect2(
                                                  url='item_fee_rate',
                                                  attrs={
                                                      'class': 'form-control form-control-sm',
                                                      'style': 'width:100%; height:100%',
                                                      'data-placeholder': '선택 및 검색',
                                                  }),
                                              )


# 설비 기준정보관리
class facilities_fm(forms.Form):

    def __init__(self, *args, **kwargs):
        super(facilities_fm, self).__init__(*args, **kwargs)
        self.enterpriseName = args[1]

    enterpriseName = '서울소프트'
    # qs_facilities = FacilitiesMaster.objects.none()
    qs_code_master = CodeMaster.objects.none()

    # search
    # 공장구분 104 code104_name_ac
    eq_factory_sch = forms.ModelChoiceField(required=False,
                                            queryset=qs_code_master,
                                            widget=autocomplete.ListSelect2(
                                                url='code104_name_ac',
                                                attrs={
                                                    'class': 'form-control form-control-sm',
                                                    'style': 'width:100%; height:100%',
                                                    'data-placeholder': '선택 및 검색',
                                                }),
                                            )

    # 공정구분 109 code109_name_ac
    eq_process_sch = forms.ModelChoiceField(required=False,
                                            queryset=qs_code_master,
                                            widget=autocomplete.ListSelect2(
                                                url='code109_name_ac',
                                                attrs={
                                                    'class': 'form-control form-control-sm',
                                                    'style': 'width:100%; height:100%',
                                                    'data-placeholder': '선택 및 검색',
                                                }),
                                            )

    # add
    # 공장구분 104 code104_name_ac
    eq_factory_add = forms.ModelChoiceField(required=False,
                                            queryset=qs_code_master,
                                            widget=autocomplete.ListSelect2(
                                                url='code104_name_ac',
                                                attrs={
                                                    'class': 'form-control form-control-sm',
                                                    'style': 'width:100%; height:100%',
                                                    'data-placeholder': '선택 및 검색',
                                                }),
                                            )

    # 공정구분 109 code109_name_ac
    eq_process_add = forms.ModelChoiceField(required=False,
                                            queryset=qs_code_master,
                                            widget=autocomplete.ListSelect2(
                                                url='code109_name_ac',
                                                attrs={
                                                    'class': 'form-control form-control-sm',
                                                    'style': 'width:100%; height:100%',
                                                    'data-placeholder': '선택 및 검색',
                                                }),
                                            )

    # 작업장 110 code110_name_ac
    eq_workshop_add = forms.ModelChoiceField(required=False,
                                             queryset=qs_code_master,
                                             widget=autocomplete.ListSelect2(
                                                 url='code110_name_ac',
                                                 attrs={
                                                     'class': 'form-control form-control-sm',
                                                     'style': 'width:100%; height:100%',
                                                     'data-placeholder': '선택 및 검색',
                                                 }),
                                             )

    # 설비타입, 설비구분 111 code111_name_ac
    eq_type_add = forms.ModelChoiceField(required=False,
                                         queryset=qs_code_master,
                                         widget=autocomplete.ListSelect2(
                                             url='code111_name_ac',
                                             attrs={
                                                 'class': 'form-control form-control-sm',
                                                 'style': 'width:100%; height:100%',
                                                 'data-placeholder': '선택 및 검색',
                                             }),
                                         )


# 납품기업
class order_company_fm(forms.Form):

    def __init__(self, *args, **kwargs):
        super(order_company_fm, self).__init__(*args, **kwargs)
        self.enterpriseName = args[1]

    enterpriseName = '서울소프트'
    qs_oc = CodeMaster.objects.none()

    # Search
    # 기업명
    oc_name_sch = forms.ModelChoiceField(required=False,
                                         queryset=qs_oc,
                                         widget=autocomplete.ListSelect2(
                                             url='oc_name_ac',
                                             attrs={
                                                 'class': 'form-control form-control-sm',
                                                 'style': 'width:100%; height:100%',
                                                 'data-placeholder': '선택 및 검색',
                                             }),
                                         )


# 의뢰서
class request_fm(forms.Form):

    def __init__(self, *args, **kwargs):
        super(request_fm, self).__init__(*args, **kwargs)
        self.enterpriseName = args[1]

    enterpriseName = '서울소프트'
    qs_customer = CodeMaster.objects.none()
    qs_item = EnterpriseMaster.objects.none()

    # 거래처 코드
    cu_code_sch = forms.ModelChoiceField(required=False,
                                         queryset=qs_customer,
                                         widget=autocomplete.ListSelect2(
                                             url='customer_code_ac',
                                             attrs={
                                                 'class': 'form-control form-control-sm',
                                                 'style': 'width:100%; height:100%',
                                                 'data-placeholder': '선택 및 검색',
                                             }),
                                         )

    # 거래처 명
    cu_name_sch = forms.ModelChoiceField(required=False,
                                         queryset=qs_customer,
                                         widget=autocomplete.ListSelect2(
                                             url='customer_name_ac',
                                             attrs={
                                                 'class': 'form-control form-control-sm',
                                                 'style': 'width:100%; height:100%',
                                                 'data-placeholder': '선택 및 검색',
                                             }),
                                         )

    # 거래처 코드 disabled
    cu_code_dis = forms.ModelChoiceField(required=False,
                                         queryset=qs_customer,
                                         widget=autocomplete.ListSelect2(
                                             url='customer_code_ac',
                                             attrs={
                                                 'class': 'form-control form-control-sm',
                                                 'style': 'width:100%; height:100%',
                                                 'data-placeholder': '선택 및 검색',
                                             }),
                                         disabled=True
                                         )

    # 거래처 명 disabled
    cu_name_dis = forms.ModelChoiceField(required=False,
                                         queryset=qs_customer,
                                         widget=autocomplete.ListSelect2(
                                             url='customer_name_ac',
                                             attrs={
                                                 'class': 'form-control form-control-sm',
                                                 'style': 'width:100%; height:100%',
                                                 'data-placeholder': '선택 및 검색',
                                             }),
                                         disabled=True
                                         )

    # 품번
    it_code_sch = forms.ModelChoiceField(required=False,
                                         queryset=qs_item,
                                         widget=autocomplete.ListSelect2(
                                             url='item_code_ac',
                                             attrs={
                                                 'class': 'form-control form-control-sm',
                                                 'style': 'width:100%; height:100%',
                                                 'data-placeholder': '선택 및 검색',
                                             }),
                                         )

    # 품명
    it_name_sch = forms.ModelChoiceField(required=False,
                                         queryset=qs_item,
                                         widget=autocomplete.ListSelect2(
                                             url='item_name_ac',
                                             attrs={
                                                 'class': 'form-control form-control-sm',
                                                 'style': 'width:100%; height:100%',
                                                 'data-placeholder': '선택 및 검색',
                                             }),
                                         )
    it_nice_number_sch = forms.ModelChoiceField(required=False,
                                                queryset=qs_item,
                                                widget=autocomplete.ListSelect2(
                                                    url='item_nice_number_ac',
                                                    attrs={
                                                        'class': 'form-control form-control-sm',
                                                        'style': 'width:100%; height:100%',
                                                        'data-placeholder': '선택 및 검색',
                                                    }),
                                                )


class enterprise_fm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(enterprise_fm, self).__init__(*args, **kwargs)
        self.enterpriseName = args[1]

    enterpriseName = '서울소프트'
    qs_enterprise = EnterpriseMaster.objects.none()

    # 회사 정보 조회
    enterprise_name_ac = forms.ModelChoiceField(required=False,
                                                queryset=qs_enterprise,
                                                widget=autocomplete.ListSelect2(
                                                    url='enterprise_name_ac',
                                                    attrs={
                                                        'class': 'form-control form-control-sm',
                                                        'style': 'width:100%; height:100%',
                                                        'data-placeholder': '선택 및 검색',
                                                    }),
                                                )

    # client 사용자 정보 조회
    client_name_ac = forms.ModelChoiceField(required=False,
                                            queryset=UserMaster.objects.none(),
                                            widget=autocomplete.ListSelect2(
                                                url='client_name_ac',
                                                attrs={
                                                    'class': 'form-control form-control-sm',
                                                    'style': 'width:100%; height:100%',
                                                    'data-placeholder': '선택 및 검색',
                                                }),
                                            )
