from businesses.services import BusinessService
from rest_framework.exceptions import ValidationError
from .models import Appointment

class AppointmentService:
    @staticmethod
    def create_appointment(business_id,user,data):
        business=BusinessService.get_owned_business(user,business_id)
        customer=data["customer"]
        offering=data["offering"]
        appointment_datetime=data["appointment_datetime"]

        if customer.business != business:
            raise ValidationError('Customer does not belong to this business')
        if offering.business != business:
            raise ValidationError('Offering does not belong to this business.')
        if Appointment.objects.filter(customer__business=business,appointment_datetime=appointment_datetime).exists(): #__ ilşki üzerinden ilerle demek appointment ile business direkt bağlantısı yok 
            raise ValidationError("An appointment already exists for this business at this time.")

        appointment=Appointment(**data)
        appointment.full_clean() #Modelde ki validationları çalıştırdı
        appointment.save() #validation geçtiyse db yaz
        return appointment



