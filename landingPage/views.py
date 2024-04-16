from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.models import User
from .models import Profile

# Create your views here.
def dashboard(request):
    return render(request, "pages/dashboard.html")

def registerSelect(request):
    return render(request, "auth/RegisterSelect.html")

def register(request):
    if request.method == "POST":
        password = request.POST.get("password")
        confirmPassword = request.POST.get("confirm-password")
        corpName = request.POST.get("corpName")
        corpNumber = request.POST.get("corpNumber")
        corpManager = request.POST.get("corpManager")
        department = request.POST.get("department")
        email = request.POST.get("email")
        username = email[:email.find("@")]
        if password == confirmPassword:
            user = User.objects.create_user(username=username, password=password, email=email)
            profile = Profile.objects.create(user=user, corpName=corpName, corpNumber=corpNumber, corpManager=corpManager, department=department, email=email)
            login(request, user)
            return redirect("dashboard")
        else:
            return render(request, "auth/register.html", {"error": "비밀번호가 일치하지 않습니다."})
    return render(request, "auth/register.html")

def register_view(request):
    return render(request, 'auth/register.html', {})