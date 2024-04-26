from django.db import models
from django.contrib.auth.models import User

from django.db import models

class UserMaster(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    password = models.CharField(max_length=255)
    user_auth_id = models.CharField(max_length=255)
    user_code = models.CharField(max_length=255)
    user_name = models.CharField(max_length=255)
    join_date = models.DateField()
    address = models.CharField(max_length=255)
    email = models.EmailField()
    tel = models.CharField(max_length=255)
    fax = models.CharField(max_length=255)
    signature = models.ImageField(upload_to='user_signatures/')
    custom_id = models.ForeignKey('CustomerMaster', on_delete=models.CASCADE)
    is_superuser = models.BooleanField(default=False)
    is_master = models.BooleanField(default=False)
    delete_flag = models.CharField(max_length=1)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    created_by_id = models.ForeignKey('self', related_name='user_created_by', on_delete=models.CASCADE)
    updated_by_id = models.ForeignKey('self', related_name='user_updated_by', on_delete=models.CASCADE)

class CustomerMaster(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=255)
    licensee_no = models.CharField(max_length=255)
    owner_name = models.CharField(max_length=255)
    bus_con = models.CharField(max_length=255)
    bus_event = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=255)
    addr = models.CharField(max_length=255)
    office_tel = models.CharField(max_length=255)
    office_fax = models.CharField(max_length=255)
    office_email = models.EmailField()
    charge_name = models.CharField(max_length=255)
    charge_tel = models.CharField(max_length=255)
    charge_pos = models.CharField(max_length=255)
    etc = models.TextField()
    cus_type = models.CharField(max_length=255)
    delete_flag = models.CharField(max_length=1)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    created_by_id = models.ForeignKey('UserMaster', related_name='customer_created_by', on_delete=models.CASCADE)
    updated_by_id = models.ForeignKey('UserMaster', related_name='customer_updated_by', on_delete=models.CASCADE)

# Create your models here.