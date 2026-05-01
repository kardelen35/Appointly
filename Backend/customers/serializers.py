from rest_framework import serializers
from .models import Customer


class CustomerSerializer(serializers.ModelSerializer):
    business_name=serializers.ReadOnlyField(source="business.name")

    class Meta:
        model=Customer
        fields = [
            "id",
            "name",
            "surname",
            "email",
            "phone",
            "business",
            "business_name",
            "is_active",
            "created_at",
        ]
        read_only_fields = [
            "business",
            "is_active",
            "created_at",
            "business_name",
        ]