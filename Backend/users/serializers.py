from .models import User
from rest_framework import serializers

class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True, max_length=190)
    full_name = serializers.CharField(required=True, max_length=190)
    password=serializers.CharField(required=True,write_only=True,min_length=6) #response dönerken gösterilmiyor write_only=True olunca 

    class Meta:
        model=User
        fields=['email','full_name','password']
    def create(self,validated_data):
        return User.objects.create_user(**validated_data)
    def validate_email(self,value):
        return value.lower()
    
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['id',"full_name","email","is_active","date_joined"]