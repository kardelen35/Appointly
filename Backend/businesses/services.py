from django.shortcuts import get_object_or_404
from rest_framework.exceptions import ValidationError
from .models import Business


class BusinessService:
    def get_owned_business(user, business_id):
        business = get_object_or_404(Business, id=business_id)

        if business.owner != user:
            raise ValidationError("You do not own this business")

        if not business.is_active:
            raise ValidationError("This business is not active")

        return business