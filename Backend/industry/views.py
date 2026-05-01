from .models import Industry
from rest_framework.generics import ListCreateAPIView
from .serializers import IndustrySerializer


# Create your views here.
class IndustryView(ListCreateAPIView):
    queryset=Industry.objects.filter(is_active=True)
    serializer_class=IndustrySerializer
