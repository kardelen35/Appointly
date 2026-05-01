
from django.urls import path
from .views import IndustryView


urlpatterns = [
    path('', IndustryView.as_view()), #class based view func çevrilir
]