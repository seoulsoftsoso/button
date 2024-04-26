from django.shortcuts import render
from django.core.paginator import Paginator
from django.http import JsonResponse

from .models import itemMaster, basicBom, BOMMaster, OrderMaster
from datetime import datetime
# Create your views here.

def delivery(request):
    return render(request, 'pages/Delivery.html')

def item (request):
    return render(request, 'pages/Item.html')

def build(request):
    return render(request, 'pages/Build.html')

def items(request):
    if request.method == "POST":
        item = request.POST.dict()
        itemMaster.objects.create(
            item_code= item['itemCode'],
            item_name=item['itemName'],
            item_type= item['itemType'],
            specification= item['specification'],
            model= item['model'],
            maker= item['maker'],
            level= item['level'],
            standard_price = item['standardPrice'],
            delete_flag = 'N',
            created_by = request.user,
            updated_by = request.user
        )
        return JsonResponse({'message': 'success'})
    elif request.method == "GET":
        items = itemMaster.objects.all()
        return JsonResponse({'data': list(items.values())})
def item_id(request, id):
    if request.method == "DELETE":
        itemMaster.objects.filter(id=id).delete()
        return JsonResponse({'message': 'success'})
    elif request.method == "PATCH":
        item = itemMaster.objects.get(id=id)
        item.update(**request.POST.dict())
        return JsonResponse({'message': 'success'})
