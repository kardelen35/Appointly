
from django.urls import path
from .views import OfferingView


urlpatterns = [
    path('<int:business_id>/offerings/', OfferingView.as_view()), #class based view func çevrilir
]