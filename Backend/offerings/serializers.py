from rest_framework import serializers
from .models import Offering


class OfferingSerializer(serializers.ModelSerializer):
    business_name=serializers.ReadOnlyField(source="business.name")
    class Meta:
        model=Offering
        fields = [
            "id",
            "name",
            "detail",
            "business",
            "business_name",
            "is_active",
        ]
        read_only_fields = [
            "is_active",
            "business",
            "business_name",
        ]