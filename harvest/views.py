from django.shortcuts import render

# Create your views here.
def FAQ(request):
    return render(request, 'pages/FAQ.html')

def Info(request):
    return render(request, 'pages/Info.html')

def Manual(request):
    return render(request, 'pages/Manual.html')