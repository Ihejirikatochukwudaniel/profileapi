from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse

def health_check(request):
    """Simple health check endpoint"""
    return JsonResponse({
        'status': 'ok',
        'message': 'Profile API is running'
    })

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', health_check, name='health_check'),  # Root URL
    path('api/', include('api.urls')),  # API endpoints
]
