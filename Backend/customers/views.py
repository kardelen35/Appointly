from rest_framework.generics import ListCreateAPIView
from .models import Customer
from .serializers import CustomerSerializer
from businesses.services import BusinessService
from .services import CustomerService

# Create your views here.
class CustomerView(ListCreateAPIView):
    serializer_class=CustomerSerializer

    def get_queryset(self):
        business_id=self.kwargs['business_id']
        user=self.request.user
        business=BusinessService.get_owned_business(user,business_id)
        return Customer.objects.filter(business=business,is_active=True)
    

    def perform_create(self, serializer):
        business_id = self.kwargs["business_id"]
        user = self.request.user
        data = serializer.validated_data
        customer = CustomerService.create_customer(user, business_id, data)
        serializer.instance = customer #save yerine artık bunu response olarak dönmeli

