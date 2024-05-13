from django.db import models

from landingPage.models import UserMaster
from django.contrib.auth.models import User

# Create your models here.
class itemMaster(models.Model):
    code = models.CharField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    specification = models.TextField(blank=True, null=True)
    model = models.TextField(blank=True, null=True)
    brand = models.CharField(max_length=255, blank=True, null=True)
    level = models.CharField(max_length=255) # root = container / 1 = controller / 2 = part(item)
    standard_price = models.IntegerField(blank=True, null=True)
    delete_flag = models.CharField(max_length=1, choices=(('Y', 'Yes'), ('N', 'No')))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, related_name='item_created_by', on_delete=models.CASCADE)
    updated_by = models.ForeignKey(User, related_name='item_updated_by', on_delete=models.CASCADE)


class basicBom(models.Model):
    code = models.CharField(max_length=255)
    level = models.IntegerField()
    item = models.ForeignKey('itemMaster', on_delete=models.CASCADE)
    parent = models.ForeignKey('basicBom', related_name='parent_bom', on_delete=models.CASCADE)
    delete_flag = models.CharField(max_length=1, choices=(('Y', 'Yes'), ('N', 'No')))

class BOMMaster(models.Model):
    level = models.IntegerField() # root = 0
    part = models.CharField(max_length=255)
    item = models.ForeignKey('ItemMaster', on_delete=models.SET_NULL, null=True)
    parent = models.ForeignKey('BOMMaster', related_name='parent_bom', on_delete=models.SET_NULL, null=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    tax = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    op = models.ForeignKey('OrderProduct', on_delete=models.SET_NULL, null=True)
    delete_flag = models.CharField(max_length=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, related_name='bom_created_by', on_delete=models.CASCADE)
    updated_by = models.ForeignKey(User, related_name='bom_updated_by', on_delete=models.CASCADE)

class OrderMaster(models.Model):
    so_no = models.CharField(max_length=255)
    client = models.ForeignKey(UserMaster, on_delete=models.SET_NULL, null=True)
    order_date = models.DateField()
    cnt = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    tax = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    status = models.CharField(max_length=1, default=1)
    place = models.CharField(max_length=255)
    comment = models.TextField()
    delete_flag = models.CharField(max_length=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, related_name='order_created_by', on_delete=models.SET_NULL, null=True)
    updated_by = models.ForeignKey(User, related_name='order_updated_by', on_delete=models.SET_NULL, null=True)

class OrderProduct(models.Model):
    unique_no = models.CharField(max_length=255)
    product_name = models.CharField(max_length=255)
    bom = models.ForeignKey('BOMMaster', on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey('OrderMaster', on_delete=models.SET_NULL, null=True)
    delivery_date = models.DateTimeField(null=True)
    order_cnt = models.IntegerField(null=True)
    crops = models.CharField(max_length=255, null=True)
    delivery_addr = models.CharField(max_length=255, null=True)
    request_note = models.TextField(null=True)
    status = models.CharField(max_length=255, null=True)
    delete_flag = models.CharField(max_length=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, related_name='order_product_created_by', on_delete=models.CASCADE)
    updated_by = models.ForeignKey(User, related_name='order_product_updated_by', on_delete=models.CASCADE)

# bomMaster를 만드는 페이지 한개 3번째 페이지와 같이 작업 중(concept) (O)
# OrderMaster를 만드는 페이지 한개 (O) 
# bomMaster와 OrderMaster를 연결하는 OrderProduct 페이지 한개 현재 만들고 있음(0)
