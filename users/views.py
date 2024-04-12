from django.shortcuts import render

# Create your views here.
def manage(request):
    return render(request, 'pages/Manage.html')

def part(request):
    return render(request, 'pages/Part.html')