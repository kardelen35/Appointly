
from django.urls import include, path
from rest_framework import routers
from .views import BusinessView


urlpatterns = [
    path('', BusinessView.as_view()), #class based view func çevrilir
]