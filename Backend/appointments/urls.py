
from django.urls import path
from .views import AppointmentView


urlpatterns = [
    path('<int:business_id>/appointments/', AppointmentView.as_view()), #class based view func çevrilir
]