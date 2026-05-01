from businesses.services import BusinessService
from rest_framework.exceptions import ValidationError
from .models import Offering

class OfferingService:
    @staticmethod
    def create_offering(business_id,user,data):
        business=BusinessService.get_owned_business(user,business_id)
        if Offering.objects.filter(name__iexact=data["name"],business=business).exists():
            raise ValidationError("This offering already exists for this business")
        offering=Offering.objects.create(**data,business=business)
        return offering


