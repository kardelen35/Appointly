from rest_framework import serializers
from .models import Appointment

class AppointmentSerializer(serializers.ModelSerializer):
    customer_name=serializers.ReadOnlyField(source="customer.name")
    offering_name=serializers.ReadOnlyField(source="offering.name")
    class Meta:
        model = Appointment
        fields = [
            "id",
            "customer",
            "customer_name",
            "offering",
            "offering_name",
            "appointment_datetime",
            "detail",
            "status",
            "created_at"
        ]
        read_only_fields = [
            "customer_name",
            "offering_name",
        ]