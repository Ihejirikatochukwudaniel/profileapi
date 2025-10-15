from django.urls import path
from .views import get_profile

urlpatterns = [
    path('me/', get_profile, name='get_profile'),  # <-- Important route
]
