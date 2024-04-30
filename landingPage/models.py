from django.db import models
from django.contrib.auth.models import User

from django.db import models

class UserMaster(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_code = models.CharField(max_length=255)
    user_name = models.CharField(max_length=255)
    join_date = models.DateField(null=True)
    address = models.CharField(max_length=255, null=True)
    tel = models.CharField(max_length=255, null=True)
    fax = models.CharField(max_length=255, null=True)
    signature = models.ImageField(upload_to='user_signatures/', null=True)
    custom = models.ForeignKey('CustomerMaster', on_delete=models.CASCADE, null=True)
    delete_flag = models.CharField(max_length=1, choices=(('Y', 'Yes'), ('N', 'No')))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    created_by_id = models.ForeignKey('self', related_name='user_created_by', on_delete=models.CASCADE)
    updated_by_id = models.ForeignKey('self', related_name='user_updated_by', on_delete=models.CASCADE)

class CustomerMaster(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=255)
    licensee_no = models.CharField(max_length=255)
    owner_name = models.CharField(max_length=255)
    bus_con = models.CharField(max_length=255, null=True)
    bus_event = models.CharField(max_length=255, null=True)
    postal_code = models.CharField(max_length=255, null=True)
    addr = models.CharField(max_length=255, null=True)
    office_tel = models.CharField(max_length=255, null=True)
    office_fax = models.CharField(max_length=255, null=True)
    office_email = models.EmailField(null=True)
    charge_name = models.CharField(max_length=255, null=True)
    charge_tel = models.CharField(max_length=255, null=True)
    charge_pos = models.CharField(max_length=255, null=True)
    etc = models.TextField(null=True)
    cus_type = models.CharField(max_length=255, null=True)
    delete_flag = models.CharField(max_length=1, choices=(('Y', 'Yes'), ('N', 'No')))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    created_by_id = models.ForeignKey('UserMaster', related_name='customer_created_by', on_delete=models.CASCADE)
    updated_by_id = models.ForeignKey('UserMaster', related_name='customer_updated_by', on_delete=models.CASCADE)

# Create your models here.