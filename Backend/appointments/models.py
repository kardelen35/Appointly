from django.db import models
from customers.models import Customer
from offerings.models import Offering
from django.core.exceptions import ValidationError
from django.utils import timezone
# Create your models here.
class Appointment(models.Model):
    STATUS_CHOICES = [
    ("scheduled", "Planlandı"),
    ("completed", "Geldi"),
    ("no_show","Gelmedi")
    ]
    customer=models.ForeignKey(Customer,on_delete=models.PROTECT)
    offering = models.ForeignKey(Offering, on_delete=models.PROTECT)
    detail=models.CharField(max_length=255,blank=True)
    appointment_datetime=models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    status=models.CharField(max_length=10,choices=STATUS_CHOICES,default="scheduled")

    def clean(self):
        if self.customer is not None and self.offering is not None:
            if self.customer.business != self.offering.business:
                raise ValidationError("Customer and offering must belong to the same business.")
            if not self.customer.is_active:
                raise ValidationError("Customer is not active.")
            if not self.offering.is_active:
                raise ValidationError("Offering is not active.")
        if self.appointment_datetime is not None:
            if self.appointment_datetime < timezone.now() and self.status == "scheduled":
                raise ValidationError("Past appointments cannot have scheduled status.")

        super().clean()
    
   