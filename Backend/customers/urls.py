
from django.urls import path
from .views import CustomerView


urlpatterns = [
    path('<int:business_id>/customers/', CustomerView.as_view()), #class based view func çevrilir
]