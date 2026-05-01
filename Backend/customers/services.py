from django.shortcuts import get_object_or_404
from rest_framework.exceptions import ValidationError

from businesses.models import Business
from businesses.services import BusinessService
from .models import Customer


class CustomerService:

    @staticmethod
    def create_customer(user, business_id, data):
        business = BusinessService.get_owned_business(user, business_id)

        if Customer.objects.filter(email=data["email"], business=business).exists():
            raise ValidationError("This customer already exists for this business")

        customer = Customer.objects.create(
            **data,
            business=business,
        )

        return customer