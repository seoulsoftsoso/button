from django.shortcuts import render
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.db.models.functions import Cast, Round
import uuid

from .models import itemMaster, basicBom, BOMMaster, OrderMaster, OrderProduct
from landingPage.models import UserMaster
from order.models import OrderProduct, OrderMaster, BOMMaster, itemMaster
from datetime import datetime
from django.db.models import F, FloatField
import json

# Create your views here.

def delivery(request):
    context = {}
    usersList = UserMaster.objects.annotate(
        value = F('id'),
        avatar = F('signature'),
        email = F('user__email')
    ).values('value', 'name', 'avatar', 'email')
    context['usersList'] = list(usersList)
    return render(request, 'pages/Delivery.html', context)

def item (request):
    return render(request, 'pages/Item.html')

def build(request, order):
    if not order:
        return render(request, 'pages/Build.html', { 'order': 0, 'orderProduct': [], 'bomMaster': [] })
    bomTree = []
    orderProduct = OrderProduct.objects.filter(order_id=order, delete_flag="N").annotate(
        qty = F('order_cnt'),
        price = Round(Cast(F('bom__item__standard_price'), FloatField()), 2),
        product_info = F('bom__item__name'),
        image = F('bom__item__brand'),
        level = F('bom__level'),
        item_id = F('bom__item_id')
    ).values('id', 'product_name', 'qty', 'price', 'product_info', 'image', 'level', 'item_id')
    bomMaster = BOMMaster.objects.filter(op__order_id=order, delete_flag='N').annotate(
        quantity = F('op__order_cnt'),
        name = F('item__name')
    ).values('id', 'item_id', 'parent_id', 'part', 'quantity', 'name').order_by('level','id')
    for (index, bom) in enumerate(bomMaster):
        if bom['parent_id'] == None:
            bom['parent_id'] = '#'
        bomTree.append({
            'id': bom['id'],
            'text': bom['part'],
            'parent': bom['parent_id'],
            'data': orderProduct[index]
        })
    context = { 'order': order, 'bomTree': bomTree }
    return render(request, 'pages/Build.html', context)

def items(request):
    if request.method == "POST":
        item = request.POST.dict()
        itemMaster.objects.create(
            code= item['code'],
            name=item['name'],
            type= item['type'],
            specification= item['specification'],
            model= item['model'],
            brand= item['brand'],
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
            place = order['place'],
            client = UserMaster.objects.get(id=order['client']),
            order_date = order['order_date'],
            cnt = order['cnt'],
            price = order['price'],
            tax = order['tax'],
            total = order['total'],
            comment = order['comment'],
            delete_flag = 'N',
            created_by = request.user,
            updated_by = request.user
        )
        return delivery(request)
    elif request.method == "GET":
        orders = OrderMaster.objects\
        .annotate(
            avatar=F('client__signature'), 
            full_name=F('client__user__username'),
            post=F('client__code')
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

def boms(request):
    if request.method == "POST":
        bom = request.POST.dict()
        BOMMaster.objects.create(
            level = bom['level'],
            part = bom['part'],
            item = itemMaster.objects.get(id=bom['item']),
            parent = basicBom.objects.get(id=bom['parent']),
            tax = bom['tax'],
            total = bom['price'],
            op = OrderMaster.objects.get(id=bom['op']),
            delete_flag = 'N',
            created_by = request.user,
            updated_by = request.user
        )
        return JsonResponse({'message': 'success'})
    elif request.method == "GET":
        boms = BOMMaster.objects.filter(delete_flag='N').values()
        return JsonResponse({'data': list(boms.values())})

def addBom(request, order):
    if request.method == "POST":
        import json
        request_data = json.loads(request.body)
        product = request_data
        level = 0
        data = product['data']
        item = itemMaster.objects.get(id=data['item_id'])
        qty = int(data['qty'])
        product['item'] = item  
        if product['parent'] == '#':
            product['parent'] = None
        else:
            parent = product['parent']
            bom = BOMMaster.objects.filter(id=parent).first()
            product['parent'] = bom
            level = bom.level + 1
        orderData = OrderProduct.objects.create(
            unique_no=str(uuid.uuid4()),
            product_name=product['text'],
            order_id=order,
            bom_id = None,
            delivery_date=datetime.now(),
            order_cnt=qty,
            delivery_addr='HCM',
            request_note='Test',
            status='1',
            delete_flag='N',
            created_by=request.user,
            updated_by=request.user
        )
        total = item.standard_price * qty
        bom = BOMMaster.objects.create(
            level = level,
            part = product['text'],
            item= item,
            parent = product['parent'],
            tax = total * 0.1,
            total = total,
            op = orderData,
            delete_flag = 'N',
            created_by = request.user,
            updated_by = request.user
        )
        orderData.bom = bom
        orderData.save()
        return JsonResponse({'message': 'success', 'order_id': orderData.id, 'bom_id': bom.id})
    elif request.method == "GET":
        orderProducts = OrderProduct.objects.filter(delete_flag='N').values()
        return JsonResponse({'data': list(orderProducts.values())})

def updateBom(request):
    if request.method == "POST":
        data = request.POST.dict()
        bom_id = data['id']
        qty = int(data['qty'])
        orderProduct = OrderProduct.objects.get(id=bom_id)
        bom = BOMMaster.objects.get(op_id = orderProduct.id)
        orderProduct.order_cnt = qty
        orderProduct.save()
        total = bom.item.standard_price * qty
        bom.total = total
        bom.tax = total * 0.1
        bom.save()
        return JsonResponse({'message': 'success'})
    
def deleteBom(request):
    if request.method == "POST":
        data = request.POST.dict()
        bom_id = data['id']
        bom = BOMMaster.objects.get(id=bom_id)
        queue = [bom]
        while queue:
            current = queue.pop()
            current.delete_flag = 'Y'
            current.save()
            orderProduct = OrderProduct.objects.get(id=current.op_id)
            orderProduct.delete_flag = 'Y'
            orderProduct.save()
            children = BOMMaster.objects.filter(parent_id=current.id)
            for child in children:
                queue.append(child)
        return JsonResponse({'message': 'success'})