from django.shortcuts import render

# Create your views here.
def breakDown(request):
    return render(request, 'pages/breakDown.html')
