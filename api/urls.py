from django.urls import path
from . import views

urlpatterns = [
    path('', views.api_root, name='api_root'),
    path('me/', views.get_profile, name='get_profile'),
    # Add more endpoints as needed
]
