from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "pages/index.html")

def authLogin(request):
    return render(request, "auth/authLoginCover.html")

def authRegisterSelect(request):
    return render(request, "auth/RegisterSelect.html")

def authRegister(request):
    return render(request, "auth/register.html")