from django.shortcuts import render

# Create your views here.
def controlError(request):
    return render(request, 'page/control.html')

def collectError(request):
    return render(request, 'page/collect.html')