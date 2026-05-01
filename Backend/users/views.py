from .serializers import RegisterSerializer,UserSerializer
from .models import User

from rest_framework.response import Response
from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import AllowAny


class RegisterView(CreateAPIView):
    permission_classes = [AllowAny]
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

class AuthUser(APIView):
    # permission_classes = [IsAuthenticated] #Sadece giriş yapmış kullanıcıların endpoint’e erişmesini sağlar
    def get(self,request):
        serializer=UserSerializer(request.user)
        return Response(serializer.data)