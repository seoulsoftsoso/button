from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
import json
from django.core.serializers.json import DjangoJSONEncoder

from django.contrib.auth.models import User
from .models import CustomerMaster, UserMaster
from pymongo import MongoClient
from order.models import BOMMaster, OrderMaster, OrderProduct, itemMaster
from django.contrib.auth.decorators import login_required

# Create your views here.
def dashboard(request):
    return render(request, "pages/dashboard.html")

def dashboard2(request):
    ########################
    om_op = OrderMaster.objects.filter(client_id=request.user.id) #1. 로그인 계정이 한 주문들.
    order_ids = om_op.values_list('id', flat=True)  #2. 1에서 id만 리스트로 만듬.
    op_oi = OrderProduct.objects.filter(order_id__in=order_ids)#3. orderProduct에서 2의 리스트에 해당되는게 있는 row만 고름.
    bom_ids = op_oi.values_list('bom_id', flat=True)#4. 3에서의 bom_id만 리스트로 만듬.
    bom_masters = BOMMaster.objects.filter(id__in=bom_ids)#5. 3을통해 드디어 로그인 계정과 관련된 BOMMaster를 골라냄.
    #######################
    bom_level_1_ids = bom_masters.filter(level=1).values_list('item_id', flat=True)#6. 5에서 level=1인 애들의 item_id를 리스트로 만듬.
    header_item_masters = itemMaster.objects.filter(id__in=bom_level_1_ids, type='A')#7. 6에서 해당되는것들이 타입A인지 itemMaster에서 골라냄.
    header_items_ids = header_item_masters.values_list('id', flat=True)#8. 7에서 골라낸것들의 id만 리스트로 만듬
    controller_bom_masters = bom_masters.filter(level=1, item_id__in=header_items_ids)
    controller_bom_ids = controller_bom_masters.values_list('id', flat=True)#9. 5중에서 타입A인것들만 추려내고 id를 리스트로 만듬
    controller_sensors_bom_masters = bom_masters.filter(parent_id__in=controller_bom_ids)#10. 봄마스터에서 parent_id가 9에서 구한것과 같은애들만 모음. 얘들은 이제 화면에 보여질 센서들.
    #11~15는 센서가 제어인지 수집인지를 구하기위한 과정.
    bom_level_2_ids = controller_sensors_bom_masters.values_list('item_id', flat=True)#11. 센서들의 item_id를 리스트로 만듬
    gtr_items = itemMaster.objects.filter(id__in=bom_level_2_ids, type='L')#12. 11에서 구한것들을 itemMaster에 비교하는데 그때의 타입이 수집인것만 분류함
    sta_items = itemMaster.objects.filter(id__in=bom_level_2_ids, type='C')#13. 11에서 구한것들을 itemMaster에 비교하는데 그때의 타입이 제어인것만 분류함
    gtr_item_ids = gtr_items.values_list('id',flat=True) #14. 12에서 구한분류에서 id만 리스트로 만듬
    sta_item_ids = sta_items.values_list('id',flat=True) #15. 13에서 구한분류에서 id만 리스트로 만듬
    #####
    gtr_bom_masters=bom_masters.objects.filter(item_id__in=gtr_item_ids) #16. 봄마스터에서 수집센서에 대한것만 분류
    sta_bom_masters=bom_masters.objects.filter(item_id__in=sta_item_ids) #17. 봄마스터에서 제어센서에 대한것만 분류

    unique_gtr_items= gtr_items.values_list('name', flat=True)
    unique_sta_items= sta_items.values_list('name', flat=True)

    print(bom_ids)
    print(request.user.id)
    # containers = BOMMaster.objects.filter(level=0)
    # sub_items = BOMMaster.objects.filter(parent__isnull=False,)

    # for bom in bommaster:


    uri = "mongodb+srv://sj:1234@cluster0.ozlwsy4.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
    client = MongoClient(uri)
    db = client['djangoConnectTest']
    dbSensorGather = db['sen_gather']
    dbSensorStatus = db['sen_status']

    unique_gtr_senids = dbSensorGather.distinct('senid')
    unique_sta_senids = dbSensorStatus.distinct('senid')
    unique_gtr_con_ids = dbSensorGather.distinct('con_id')
    unique_sta_con_ids = dbSensorStatus.distinct('con_id')

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
    return render(request, "auth/registerSelect.html")

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
            UserMaster.objects.create(user=user, code=licensee_no, name=customer_name, join_date=None, address=None, tel=None, fax=None, custom=None, delete_flag='N', created_by=user, updated_by=user)  
            login(request, user)
            return redirect("dashboard")
        else:
            return render(request, "auth/register.html", {"error": "비밀번호가 일치하지 않습니다."})
    return render(request, "auth/register.html")

def register_view(request):
    return render(request, 'auth/register.html', {})