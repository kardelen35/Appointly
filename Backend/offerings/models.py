from django.db import models
from businesses.models import Business

# Create your models here.
class Offering(models.Model):
    name=models.CharField(max_length=255)
    detail=models.TextField(max_length=255,blank=True)
    business=models.ForeignKey(Business,on_delete=models.PROTECT)
    is_active=models.BooleanField(default=True)
