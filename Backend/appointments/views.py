from rest_framework.generics import ListCreateAPIView
from .serializers import AppointmentSerializer
from .models import Appointment
from businesses.services import BusinessService
from .services import AppointmentService

# Create your views here.
class AppointmentView(ListCreateAPIView):
    serializer_class=AppointmentSerializer

    def get_queryset(self): #list
        business_id=self.kwargs['business_id']
        user=self.request.user
        business=BusinessService.get_owned_business(user,business_id)
        return Appointment.objects.filter(customer__business=business).order_by("appointment_datetime")
    
    def perform_create(self, serializer):
        business_id = self.kwargs["business_id"]
        user = self.request.user
        data = serializer.validated_data
        appointment=AppointmentService.create_appointment(business_id,user,data)
        serializer.instance=appointment
    