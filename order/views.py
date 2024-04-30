from django.shortcuts import render
from django.core.paginator import Paginator
from django.http import JsonResponse

from .models import itemMaster, basicBom, BOMMaster, OrderMaster
from landingPage.models import UserMaster
from datetime import datetime
from django.db.models import F
import json
# Create your views here.

def delivery(request):
    return render(request, 'pages/Delivery.html')

def item (request):
    return render(request, 'pages/Item.html')

def build(request):
    context = {}
    return render(request, 'pages/Build.html', context)

def items(request):
    if request.method == "POST":
        item = request.POST.dict()
        itemMaster.objects.create(
            item_code= item['item_code'],
            item_name=item['item_name'],
            item_type= item['item_type'],
            specification= item['specification'],
            model= item['model'],
            maker= item['maker'],
            level= item['level'],
            standard_price = item['standard_price'],
            delete_flag = 'N',
            created_by = request.user,
            updated_by = request.user
        )
        return JsonResponse({'message': 'success'})
    elif request.method == "GET":
        items = itemMaster.objects.filter(delete_flag='N').values()
        return JsonResponse({'data': list(items.values())})
    
def item_edit(request, id):
        data = request.POST.dict()
        item = itemMaster.objects.get(id=id)
        for key in data:
            item.__dict__[key] = data[key]
        item.save()
        return JsonResponse({'message': 'success'})

def item_delete(request, id):
    item = itemMaster.objects.get(id=id)
    item.delete_flag = 'Y'
    item.save()
    return JsonResponse({'message': 'success'})

def orders(request):
    if request.method == "POST":
        order = request.POST.dict()
        so_no = 'BF' + str(datetime.now().strftime('%y%m%d'))
        order['client'] = json.loads(order['client'])
        order['client'] = order['client'][0]['value']
        OrderMaster.objects.create(
            so_no = so_no,
            order_delivery_place = order['order_delivery_place'],
            client = UserMaster.objects.get(id=order['client']),
            order_date = order['order_date'],
            order_cnt = order['order_cnt'],
            order_price = order['order_price'],
            order_tax = order['order_tax'],
            order_total = order['order_total'],
            comment = order['comment'],
            delete_flag = 'N',
            created_by = request.user,
            updated_by = request.user
        )
        return JsonResponse({'message': 'success'})
    elif request.method == "GET":
        orders = OrderMaster.objects\
        .annotate(
            avatar=F('client__signature'), 
            full_name=F('client__user__username'),
            post=F('client__user_code')
            )\
        .filter(delete_flag='N')\
        .values()
        return JsonResponse({'data': list(orders.values())})

def order_edit(request, id):
    data = request.POST.dict()
    order = OrderMaster.objects.get(id=id)
    for key in data:
        order.__dict__[key] = data[key]
    order.save()
    return JsonResponse({'message': 'success'})

def order_delete(request, id):
    order = OrderMaster.objects.get(id=id)
    order.delete_flag = 'Y'
    order.save()
    return JsonResponse({'message': 'success'})