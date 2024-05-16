from django.shortcuts import render
from django.http import JsonResponse
from landingPage.models import UserMaster
from django.db.models import F
# Create your views here.
def manage(request):
    return render(request, 'pages/Manage.html')

def part(request):
    return render(request, 'pages/Part.html')

def user(request):
    users = UserMaster.objects.all().annotate(
        email = F('user__email')
    )
    return JsonResponse(list(users.values()), safe=False)

def userEdit(request):
    if request.method == 'POST':
        user = UserMaster.objects.get(id = request.POST['id'])
        user.email = request.POST['email']
        user.save()
        return JsonResponse({'status': 'success'})