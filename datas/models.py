from django.db import models
from landingPage.models import UserMaster
from order.models import BOMMaster
# Create your models here.

class PlanPart(models.Model):
    name = models.CharField(max_length=100)
    part = models.ForeignKey(BOMMaster, on_delete=models.SET_NULL, null=True)
    delete_flag = models.CharField(max_length=1, default='N')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(UserMaster, related_name='created_planparts', on_delete=models.CASCADE)
    updated_by = models.ForeignKey(UserMaster, related_name='updated_planparts', on_delete=models.CASCADE)

class Plantation(models.Model):
    code = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=100)
    owner = models.CharField(max_length=100)
    part = models.ForeignKey(PlanPart, on_delete=models.SET_NULL, null=True)
    bom = models.ForeignKey(BOMMaster, on_delete=models.SET_NULL, null=True)
    delete_flag = models.CharField(max_length=1, default='N')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(UserMaster, related_name='created_plantations', on_delete=models.CASCADE)
    updated_by = models.ForeignKey(UserMaster, related_name='updated_plantations', on_delete=models.CASCADE)
