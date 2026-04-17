
from django.urls import include, path
from rest_framework import routers
from .views import RegisterView,AuthUser


urlpatterns = [
    path('register/', RegisterView.as_view()), #class based view func çevrilir
    path('me/',AuthUser.as_view())
]