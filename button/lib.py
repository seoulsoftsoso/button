from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def Pagenation(queryset, _size=20, _page=0, _range=5):
    _size = int(_size)  # 20? 개 리스트 보여주기
    _page = int(_page)  # 선택한 페이지 보여주기
    _range = int(_range)  # 하단에 표시되는 페이지네이션 범위 수

    paginator = Paginator(queryset, _size)

    try:
        queryset = paginator.page(_page)
    except PageNotAnInteger:
        queryset = paginator.page(1)
    except EmptyPage:
        queryset = paginator.page(paginator.num_pages)

    return queryset


def PaginatorManager(request, queryset, num=20, pagenum=0):

    if num == "":
         num = 20
    if pagenum == 0:
        pagenum = request.GET.get('page', 1)
        if pagenum == '':
            pagenum = 1

    page = int(pagenum)

    paginator = Paginator(queryset, num)

    max_index = len(paginator.page_range)
    current_page = int(page) if page else 1
    page_numbers_range = 5  # Display only 5 page numbers

    start_index = int((current_page - 1) / page_numbers_range) * page_numbers_range
    end_index = start_index + page_numbers_range

    if end_index >= max_index:
        end_index = max_index

    page_range = paginator.page_range[start_index:end_index]
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        queryset = paginator.page(1)
    except EmptyPage:
        queryset = paginator.page(paginator.num_pages)

    return page_range, queryset
