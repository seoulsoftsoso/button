from numpy import long
from rest_framework.permissions import BasePermission


class MesPermission(BasePermission):
    """
    권한은 String 이며, 문자 '1'과 '0' 만을 사용합니다. 아래와 같은 규칙이 적용됩니다.
      해당 index 가 1이면 허용, 0이면 비허용입니다.
      index : 0 - 코드마스터
      index : 1 - 거래처_기준정보관리
      index : 2 - 사용자_기준정보관리
      index : 3 - 설비_기준정보관리
      index : 4 - 품목_기준정보관리
      index : 5 - 사용자_권한관리
      index : 6 - BOM_형식
      index : 7 - BOM_관리
      index : 8 - BOM_조회
      ...

    현재는 100번째까지 사용할 수 있습니다. 그 이상을 사용하시려면,
    EnterpriseMaster 모델의 permissions 과  UserMaster 모델의 permissions 의 max_length 를 변경 하세요.
      그리고 PERMISSION_DEFAULT 를 검색해서 초기값을 재지정 바랍니다.
      let PERMISSION_DEFAULT = '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000';

    예를들어 1110000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 인 경우
      코드마스터, 거래처_기준정보관리, 사용자_기준정보관리 만 허가된 것입니다.

    return True : # 사용 권한이 있는 경우
    return False : # 사용 권한이 없는 경우

    """

    def has_permission(self, request, view):
        given = request.user.permissions
        requested_viewset = view.__class__.__name__

        if request.user.is_superuser == True:
            return True

        if requested_viewset == 'EnterpriseMasterViewSet':
            return True

        elif requested_viewset == 'CodeMasterViewSet':
            return True

        elif requested_viewset == 'GroupCodeMasterViewSet':
            if given[0] == '1': return True  # 코드_마스터
            return False

        elif requested_viewset == 'GenerateCodeMaster':
            if given[0] == '1': return True  # 코드_마스터
            return False

        elif requested_viewset == 'UserMasterViewSet':
            return True
        return True

        # TODO : hjlim 추후에 문제 발생 시 수정 할 계획

        # elif requested_viewset == 'CustomerMasterViewSet':
        #     if given[1] == '1': return True  # 거래처_기준정보관리
        #     if given[4] == '1': return True  # 품목_기준정보관리
        #     if given[47] == '1': return True  # 의뢰서작성
        #     if given[48] == '1': return True  # 의뢰서조회
        #     if given[49] == '1': return True  # 견적서작성
        #     if given[50] == '1': return True  # 견적서조회
        #     if given[36] == '1': return True  # 주문서등록
        #     if given[37] == '1': return True  # 주문현황조회
        #     if given[31] == '1': return True  # 발주등록
        #     if given[32] == '1': return True  # 발주대비_입고등록
        #     if given[33] == '1': return True  # 발주대비_입고현황
        #     if given[6] == '1': return True  # BOM_형식_생성
        #     if given[7] == '1': return True  # BOM_관리
        #     if given[8] == '1': return True  # BOM_조회
        #     if given[9] == '1': return True  # BOM_재고현황
        #     if given[10] == '1': return True  # 재고입고
        #     if given[11] == '1': return True  # 재고출고
        #     if given[13] == '1': return True  # 재고현황
        #     if given[14] == '1': return True  # 재고조정
        #     if given[15] == '1': return True  # 공정명등록관리
        #     if given[43] == '1': return True  # 출하등록
        #     if given[44] == '1': return True  # 출하내역조회
        #     if given[45] == '1': return True  # 제품별원가
        #     if given[46] == '1': return True  # 주문대비원가
        #     if given[20] == '1': return True  # 대여_등록_회수_관리
        #     if given[21] == '1': return True  # 대여현황_조회
        #     return False
        #
        # elif requested_viewset == 'FacilitiesMasterViewSet':
        #     if given[3] == '1': return True  # 설비_기준정보관리
        #     if given[22] == '1': return True  # 온습도_모니터링_장비관리
        #     if given[23] == '1': return True  # 온습도_현황_조회
        #     if given[24] == '1': return True  # 온습도_현황_조회_tv
        #     if given[28] == '1': return True  # 온도전압_장비관리
        #     if given[29] == '1': return True  # 온도전압_현황조회
        #     if given[30] == '1': return True  # 온도전압_이력조회
        #     return False
        #
        # elif requested_viewset == 'ItemMasterViewSet':
        #     if given[4] == '1': return True  # 품목_기준정보관리
        #     if given[47] == '1': return True  # 의뢰서작성
        #     if given[49] == '1': return True  # 견적서작성
        #     if given[50] == '1': return True  # 견적서조회
        #     if given[36] == '1': return True  # 주문서등록
        #     if given[37] == '1': return True  # 주문현황조회
        #     if given[31] == '1': return True  # 발주등록
        #     if given[7] == '1': return True  # BOM_관리
        #     if given[10] == '1': return True  # 재고입고
        #     if given[11] == '1': return True  # 재고출고
        #     if given[12] == '1': return True  # 재고반입
        #     if given[13] == '1': return True  # 재고현황
        #     if given[14] == '1': return True  # 재고조정
        #     if given[45] == '1': return True  # 제품별원가
        #     if given[19] == '1': return True  # 대여품목_관리
        #     if given[20] == '1': return True  # 대여_등록_회수_관리
        #     if given[21] == '1': return True  # 대여현황_조회
        #     return False
        #
        # elif requested_viewset == 'OrderCompanyViewSet':
        #     if given[42] == '1': return True  # 납품기업
        #     if given[28] == '1': return True  # 온도전압_장비관리
        #     if given[29] == '1': return True  # 온도전압_현황조회
        #     if given[30] == '1': return True  # 온도전압_이력조회
        #     return False
        #
        # elif requested_viewset == 'MyInfoViewSet':
        #     if given[57] == '1': return True  # 내정보
        #     if given[50] == '1': return True  # 견적서조회
        #     if given[31] == '1': return True  # 발주등록
        #     if given[44] == '1': return True  # 출하내역조회
        #     return False
        #
        # elif requested_viewset == 'RequestViewSet':
        #     if given[47] == '1': return True  # 의뢰서작성
        #     if given[48] == '1': return True  # 의뢰서조회
        #     return False
        #
        # elif requested_viewset == 'RequestItemsViewSet':
        #     if given[48] == '1': return True  # 의뢰서조회
        #     if given[49] == '1': return True  # 견적서작성
        #     return False
        #
        # elif requested_viewset == 'EstimateViewSet':
        #     if given[49] == '1': return True  # 견적서작성
        #     if given[50] == '1': return True  # 견적서조회
        #     return False
        #
        # elif requested_viewset == 'EstimateItemsViewSet':
        #     if given[50] == '1': return True  # 견적서조회
        #     if given[36] == '1': return True  # 주문서등록
        #     return False
        #
        # elif requested_viewset == 'OrderingViewSet':
        #     if given[36] == '1': return True  # 주문서등록
        #     if given[37] == '1': return True  # 주문현황조회
        #     if given[43] == '1': return True  # 출하등록
        #     if given[44] == '1': return True  # 출하내역조회
        #     if given[46] == '1': return True  # 주문대비원가
        #     return False
        #
        # elif requested_viewset == 'OrderingItemsViewSet':
        #     if given[37] == '1': return True  # 주문현황조회
        #     if given[43] == '1': return True  # 출하등록
        #     if given[46] == '1': return True  # 주문대비원가
        #     return False
        #
        # elif requested_viewset == 'OrdersViewSet':
        #     if given[31] == '1': return True  # 발주등록
        #     if given[32] == '1': return True  # 발주대비_입고등록
        #     if given[33] == '1': return True  # 발주대비_입고현황
        #     return False
        #
        # elif requested_viewset == 'OrdersItemsViewSet':
        #     if given[31] == '1': return True  # 발주등록
        #     if given[32] == '1': return True  # 발주대비_입고등록
        #     if given[33] == '1': return True  # 발주대비_입고현황
        #     return False
        #
        # elif requested_viewset == 'OrdersInItemsViewSet':
        #     if given[32] == '1': return True  # 발주대비_입고등록
        #     if given[33] == '1': return True  # 발주대비_입고현황
        #     return False
        #
        # elif requested_viewset == 'BomMasterViewSet':
        #     if given[6] == '1': return True  # BOM_형식_생성
        #     if given[7] == '1': return True  # BOM_관리
        #     if given[8] == '1': return True  # BOM_조회
        #     if given[9] == '1': return True  # BOM_재고현황
        #     if given[10] == '1': return True  # 재고입고
        #     if given[15] == '1': return True  # 공정명등록관리
        #     if given[16] == '1': return True  # 생산일정등록
        #     if given[17] == '1': return True  # 공정진행현황등록
        #     if given[58] == '1': return True  # 공정진행현황등록(tablet)
        #     if given[18] == '1': return True  # 공정진행현황조회
        #     if given[56] == '1': return True  # 공정진행현황조회TV
        #     if given[45] == '1': return True  # 제품별원가
        #     return False
        #
        # elif requested_viewset == 'BomViewSet':
        #     if given[7] == '1': return True  # BOM_관리
        #     if given[8] == '1': return True  # BOM_조회
        #     return False
        #
        # elif requested_viewset == 'BomItemViewSet':
        #     if given[9] == '1': return True  # BOM_재고현황
        #     return False
        #
        # elif requested_viewset == 'ItemInViewSet':
        #     if given[10] == '1': return True  # 재고입고
        #     return False
        #
        # elif requested_viewset == 'ItemOutViewSet':
        #     if given[11] == '1': return True  # 재고출고
        #     return False
        #
        # elif requested_viewset == 'ItemReinViewSet':
        #     if given[12] == '1': return True  # 재고반입
        #     return False
        #
        # elif requested_viewset == 'ItemCalculateViewSet':
        #     if given[13] == '1': return True  # 재고현황
        #     if given[59] == '1': return True  # 재고현황(TV)
        #     return False
        #
        # elif requested_viewset == 'ItemMasterAdjustViewSet':
        #     if given[14] == '1': return True  # 재고조정
        #     return False
        #
        # elif requested_viewset == 'ItemAdjustViewSet':
        #     if given[14] == '1': return True  # 재고조정
        #     return False
        #
        # elif requested_viewset == 'SubprocessTempletViewSet':
        #     if given[15] == '1': return True  # 공정명등록관리
        #     return False
        #
        # elif requested_viewset == 'ProcessManagementViewSet':
        #     if given[16] == '1': return True  # 생산일정등록
        #     if given[17] == '1': return True  # 공정진행현황등록
        #     if given[58] == '1': return True  # 공정진행현황등록(tablet)
        #     return False
        #
        # elif requested_viewset == 'SubprocessManagementViewSet':
        #     if given[16] == '1': return True  # 생산일정등록
        #     if given[17] == '1': return True  # 공정진행현황등록
        #     if given[58] == '1': return True  # 공정진행현황등록(tablet)
        #     return False
        #
        # elif requested_viewset == 'ProcessStatusViewSet':
        #     if given[18] == '1': return True  # 공정진행현황조회
        #     if given[56] == '1': return True  # 공정진행현황조회TV
        #     return False
        #
        # elif requested_viewset == 'OrderingExItemsViewSet':
        #     if given[43] == '1': return True  # 출하등록
        #     if given[44] == '1': return True  # 출하내역조회
        #     return False
        #
        # elif requested_viewset == 'CostProductViewSet':
        #     if given[45] == '1': return True  # 제품별원가
        #     return False
        #
        # elif requested_viewset == 'ItemCostCalculateViewSet':
        #     if given[45] == '1': return True  # 제품별원가
        #     return False
        #
        # elif requested_viewset == 'SensorViewSet':
        #     if given[22] == '1': return True  # 온습도_모니터링_장비관리
        #     if given[23] == '1': return True  # 온습도_현황_조회
        #     if given[24] == '1': return True  # 온습도_현황_조회_tv
        #     return False
        #
        # elif requested_viewset == 'SensorValueViewSet':
        #     if given[22] == '1': return True  # 온습도_모니터링_장비관리
        #     if given[23] == '1': return True  # 온습도_현황_조회
        #     if given[24] == '1': return True  # 온습도_현황_조회_tv
        #     return False
        #
        # elif requested_viewset == 'SensorH2ViewSet':
        #     if given[39] == '1': return True  # 온습도_모니터링_장비관리_H2
        #     if given[40] == '1': return True  # 온습도_현황_조회_H2
        #     if given[41] == '1': return True  # 온습도_현황_조회_tv_H2
        #     return False
        #
        # elif requested_viewset == 'SensorH2ValueViewSet':
        #     if given[39] == '1': return True  # 온습도_모니터링_장비관리_H2
        #     if given[40] == '1': return True  # 온습도_현황_조회_H2
        #     if given[41] == '1': return True  # 온습도_현황_조회_tv_H2
        #     return False
        #
        # elif requested_viewset == 'SensorPCViewSet':
        #     if given[28] == '1': return True  # 온도전압_장비관리
        #     if given[29] == '1': return True  # 온도전압_현황조회
        #     if given[30] == '1': return True  # 온도전압_이력조회
        #     return False
        #
        # elif requested_viewset == 'SensorPCValueViewSet':
        #     if given[28] == '1': return True  # 온도전압_장비관리
        #     if given[29] == '1': return True  # 온도전압_현황조회
        #     if given[30] == '1': return True  # 온도전압_이력조회
        #     return False
        #
        # elif requested_viewset == 'RentalMasterViewSet':
        #     if given[46] == '1': return True  # 주문대비원가
        #     if given[19] == '1': return True  # 대여품목_관리
        #     if given[20] == '1': return True  # 대여_등록_회수_관리
        #     if given[21] == '1': return True  # 대여현황_조회
        #     return False
        #
        # elif requested_viewset == 'RentalViewSet':
        #     if given[20] == '1': return True  # 대여_등록_회수_관리
        #     if given[21] == '1': return True  # 대여현황_조회
        #     return False
        #
        # elif requested_viewset == 'UnbalanceViewSet':
        #     if given[51] == '1': return True  # UNBALANCE_등록
        #     if given[52] == '1': return True  # UNBALANCE_조회
        #     return False
        #
        # elif requested_viewset == 'UnbalanceDetailViewSet':
        #     if given[51] == '1': return True  # UNBALANCE_등록
        #     return False
        #
        # elif requested_viewset == 'RotatorViewSet':
        #     if given[53] == '1': return True  # 회전자검사_관리
        #     return False
        #
        # elif requested_viewset == 'StatorViewSet':
        #     if given[55] == '1': return True  # 고정자검사_관리
        #     return False
        #
        # elif requested_viewset == 'OrderViewSet':  # 메일전송
        #     if given[49] == '1': return True  # 견적서작성
        #     if given[50] == '1': return True  # 견적서조회
        #     if given[31] == '1': return True  # 발주등록
        #     return False
        #
        # return True  # 권한이 없는 경우