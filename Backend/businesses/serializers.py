from .models import Business
from rest_framework import serializers

class BusinessSerializer(serializers.ModelSerializer):
    owner_name = serializers.ReadOnlyField(source="owner.full_name") #Bu field sadece response’ta vardır, request’te gönderilmez / kabul edilmez.
    industry_name = serializers.ReadOnlyField(source="industry.name")
    class Meta:
        model = Business
        fields = "__all__"
        read_only_fields = ["owner"] #requestte gönderilemez client değil server kontrol etmeli 