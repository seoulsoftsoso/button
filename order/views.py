from django.shortcuts import render

# Create your views here.

def delivery(request):
    return render(request, 'pages/Delivery.html')

def item (request):
    return render(request, 'pages/Item.html')
