from rest_framework.generics import ListCreateAPIView
from businesses.models import Business
from .serializers import BusinessSerializer


class BusinessView(ListCreateAPIView):
    serializer_class = BusinessSerializer

    def get_queryset(self):
        return Business.objects.filter(
            owner=self.request.user,
            is_active=True
        )

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)