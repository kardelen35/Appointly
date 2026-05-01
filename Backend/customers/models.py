from django.db import models
from businesses.models import Business


class Customer(models.Model):
    
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    business = models.ForeignKey(Business, on_delete=models.PROTECT)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["business", "email"],
                name="unique_customer_email_per_business",
            )
        ]
    def __str__(self):
        return self.name