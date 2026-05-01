from django.db import models
from users.models import User
from industry.models import Industry
from django.utils.text import slugify
from django.core.exceptions import ValidationError

class Business(models.Model):
    industry = models.ForeignKey(Industry, on_delete=models.PROTECT)
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(User, on_delete=models.PROTECT)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=15, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True, blank=True)
    is_active = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def clean(self):
        if self.owner and not self.owner.is_active:
            raise ValidationError("Owner must be active.")

        if self.industry and not self.industry.is_active:
            raise ValidationError("Industry must be active.")

        if self.owner and self.owner.role != "owner":
            raise ValidationError("User must have owner role to create a business.")

        super().clean()

    def __str__(self):
        return self.name