from django.shortcuts import render

# Create your views here.
def auto(request):
    return render(request, 'pages/Auto.html')
