import decimal

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

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


def lib_generate_code(prefix1, model, model_field_prefix, user):
    from datetime import date
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



def rounds(_x, _y):  # x : 숫자값, y : 자릿수

    import numpy as np
    # x = np.floor(_x * 100) / 100
    ret = round(decimal.Decimal(_x), 2)

    return float(ret)


def round2(num):
    ret = 0

    try:
        num = float(num)

    except Exception as e:
        return 0

    minus = True if (num < 0) else False
    if minus == True:
        num = num * -1

    ret = int(num) + (1 if num - int(num) >= 0.5 else 0)

    if minus == True:
        ret = ret * -1

    return ret


# 소수점 반올림
def tof(_x, _y): # x : 숫자값, y : 소수점 자릿수
    try:
        _x = float(_x)
        _y = int(_y)

        if _y <= 0:
            _y = 0

    except:
        return 0

    mul = 1
    for i in range(0, _y):
        mul *= 10

    _x = _x * mul * 10
    x = round2(_x)  # 소수점 한번 더 에서 반올림
    x = x / 10

    x = round2(x)
    x = x / mul

    return x