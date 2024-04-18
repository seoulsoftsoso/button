from django.shortcuts import render

# Create your views here.
def deviceControl(request):
    return render(request, 'pages/DeviceControl.html')

def deviceExplain(request):
    return render(request, 'pages/DeviceExplain.html')

def delivery(request):
    return render(request, 'pages/Delivery.html')

def item (request):
    return render(request, 'pages/Item.html')
