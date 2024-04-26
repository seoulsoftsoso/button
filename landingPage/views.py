from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.models import User
from .models import CustomerMaster, UserMaster

# Create your views here.
def dashboard(request):
    return render(request, "pages/dashboard.html")

def registerSelect(request):
    return render(request, "auth/RegisterSelect.html")

def register(request):
    if request.method == "POST":
        password = request.POST.get("password")
        confirmPassword = request.POST.get("confirm-password")
        customer_name = request.POST.get("customer_name")
        licensee_no = request.POST.get("licensee_no")
        owner_name = request.POST.get("owner_name")
        charge_pos = request.POST.get("charge_pos")
        email = request.POST.get("email")
        username = email[:email.find("@")]
        if password == confirmPassword:
            user = User.objects.create_user(username=username, password=password, email=email)
            UserMaster.objects.create(user=user, custom_name=customer_name, licensee_no=licensee_no, owner_name=owner_name, charge_name=charge_pos, office_email=email)
            login(request, user)
            return redirect("dashboard")
        else:
            return render(request, "auth/register.html", {"error": "비밀번호가 일치하지 않습니다."})
    return render(request, "auth/register.html")

def register_view(request):
    return render(request, 'auth/register.html', {})