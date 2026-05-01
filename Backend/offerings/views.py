from rest_framework.generics import ListCreateAPIView
from .serializers import OfferingSerializer
from businesses.services import BusinessService
from .services import OfferingService
from .models import Offering

# Create your views here.
class OfferingView(ListCreateAPIView):
    serializer_class=OfferingSerializer

    def get_queryset(self): #listeleme için 
        business_id=self.kwargs['business_id']
        user=self.request.user
        business=BusinessService.get_owned_business(user,business_id)
        return Offering.objects.filter(business=business,is_active=True)
    
    def perform_create(self, serializer):
        business_id = self.kwargs["business_id"]
        user = self.request.user
        data = serializer.validated_data
        offering = OfferingService.create_offering(business_id, user, data)
        serializer.instance = offering