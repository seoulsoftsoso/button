from django.db import models

from django.contrib.auth.models import User

# Create your models here.
class itemMaster(models.Model):
    item_code = models.CharField(max_length=255, unique=True)
    item_name = models.CharField(max_length=255)
    item_type = models.CharField(max_length=255)
    specification = models.TextField(blank=True, null=True)
    model = models.TextField(blank=True, null=True)
    maker = models.CharField(max_length=255, blank=True, null=True)
    level = models.CharField(max_length=255)
    standard_price = models.IntegerField(blank=True, null=True)
    delete_flag = models.CharField(max_length=1, choices=(('Y', 'Yes'), ('N', 'No')))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, related_name='item_created_by', on_delete=models.CASCADE)
    updated_by = models.ForeignKey(User, related_name='item_updated_by', on_delete=models.CASCADE)


class basicBom(models.Model):
    code_name = models.CharField(max_length=255)
    level = models.IntegerField()
    item = models.ForeignKey('itemMaster', on_delete=models.CASCADE)
    parent = models.ForeignKey('basicBom', related_name='parent_bom', on_delete=models.CASCADE)
    child = models.ForeignKey('basicBom', related_name='child_bom', on_delete=models.CASCADE)
    delete_flag = models.CharField(max_length=1, choices=(('Y', 'Yes'), ('N', 'No')))

class BOMMaster(models.Model):
    level = models.IntegerField()
    part_name = models.CharField(max_length=255)
    item = models.ForeignKey('ItemMaster', on_delete=models.CASCADE)
    parent = models.ForeignKey('BOMMaster', related_name='parent_bom', on_delete=models.CASCADE)
    child = models.ForeignKey('BOMMaster', related_name='child_bom', on_delete=models.CASCADE)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    tax = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    op = models.ForeignKey('OrderProduct', on_delete=models.CASCADE)
    delete_flag = models.CharField(max_length=1)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    created_by = models.ForeignKey(User, related_name='bom_created_by', on_delete=models.CASCADE)
    updated_by = models.ForeignKey(User, related_name='bom_updated_by', on_delete=models.CASCADE)

class OrderMaster(models.Model):
    so_no = models.CharField(max_length=255)
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    order_date = models.DateTimeField()
    order_cnt = models.IntegerField()
    order_price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    order_tax = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    order_total = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    comment = models.TextField()
    delete_flag = models.CharField(max_length=1)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    created_by = models.ForeignKey(User, related_name='order_created_by', on_delete=models.CASCADE)
    updated_by = models.ForeignKey(User, related_name='order_updated_by', on_delete=models.CASCADE)

class OrderProduct(models.Model):
    unique_no = models.CharField(max_length=255)
    product_name = models.CharField(max_length=255)
    bom = models.ForeignKey('BOMMaster', on_delete=models.CASCADE)
    order = models.ForeignKey('OrderMaster', on_delete=models.CASCADE)
    delivery_date = models.DateTimeField(null=True)
    order_cnt = models.IntegerField(null=True)
    delivery_addr = models.CharField(max_length=255, null=True)
    request_note = models.TextField(null=True)
    status = models.CharField(max_length=255, null=True)
    delete_flag = models.CharField(max_length=1)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    created_by = models.ForeignKey(User, related_name='order_product_created_by', on_delete=models.CASCADE)
    updated_by = models.ForeignKey(User, related_name='order_product_updated_by', on_delete=models.CASCADE)
