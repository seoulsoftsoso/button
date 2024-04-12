from django.shortcuts import render

# Create your views here.
def control(request):
    return render(request, 'pages/Control.html')

def plan(request):
    return render(request, 'pages/Plan.html')

def Contact(request):
    return render(request, 'pages/Contact.html')

def etc (request):
    return render(request, 'pages/Etc.html')