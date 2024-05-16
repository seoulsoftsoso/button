from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
import json
from django.core.serializers.json import DjangoJSONEncoder

from django.contrib.auth.models import User
from .models import CustomerMaster, UserMaster
from pymongo import MongoClient

# Create your views here.
def dashboard(request):
    return render(request, "pages/dashboard.html")

def dashboard2(request):
    uri = "mongodb+srv://sj:1234@cluster0.ozlwsy4.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
    client = MongoClient(uri)
    db = client['djangoConnectTest']
    dbSensorGather = db['sen_gather']
    dbSensorStatus = db['sen_status']

    unique_gtr_senids = dbSensorGather.distinct('senid')
    unique_sta_senids = dbSensorStatus.distinct('senid')
    unique_gtr_con_ids = dbSensorGather.distinct('con_id')
    unique_sta_con_ids = dbSensorStatus.distinct('con_id')
    unique_val_ids = dbSensorGather.distinct('value')

    # Create a dictionary to store con_id as key and associated senid list as value
    con_id_senid_map = {}
    for con_id in unique_gtr_con_ids:
        senids = dbSensorGather.distinct('senid', {'con_id': con_id})
        senid_grt_value_map = {}
        for senid in senids:
            newest_value = dbSensorGather.find_one({'con_id': con_id, 'senid': senid}, sort=[('c_date', -1)])
            if newest_value:
                senid_grt_value_map[senid] = newest_value['value']
        con_id_senid_map[con_id] = senid_grt_value_map

    for con_id in unique_sta_con_ids:
        senids = dbSensorStatus.distinct('senid', {'con_id': con_id})
        senid_sta_value_map = {}
        for senid in senids:
            newest_value = dbSensorStatus.find_one({'con_id': con_id, 'senid': senid}, sort=[('c_date', -1)])
            if newest_value:
                senid_sta_value_map[senid] =newest_value['status']
        con_id_senid_map.setdefault(con_id, {}).update(senid_sta_value_map)
    initial_data = {
        'unique_gtr_senids': unique_gtr_senids,
        'unique_sta_senids': unique_sta_senids,
        'con_id_senid_map': con_id_senid_map
    }

    initial_data_json = json.dumps(initial_data, cls=DjangoJSONEncoder)

    return render(request, "pages/dashboard2.html", {'initial_data_json': initial_data_json})

    # return render(request, "pages/dashboard2.html",
    #               {'unique_gtr_senids': unique_gtr_senids, 'unique_sta_senids': unique_sta_senids,
    #                'con_id_senid_map': con_id_senid_map})


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
            UserMaster.objects.create(user=user, user_code=licensee_no, user_name=customer_name, join_date=None, address=None, tel=None, fax=None, custom=None, delete_flag='N', created_by=user, updated_by=user)  
            login(request, user)
            return redirect("dashboard")
        else:
            return render(request, "auth/register.html", {"error": "비밀번호가 일치하지 않습니다."})
    return render(request, "auth/register.html")

def register_view(request):
    return render(request, 'auth/register.html', {})