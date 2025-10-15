from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
import json

def api_root(request):
    """API root endpoint showing available endpoints"""
    return JsonResponse({
        'message': 'Welcome to Profile API',
        'endpoints': {
            'profile': '/api/me/',
            'health': '/',
        }
    })

@csrf_exempt
@require_http_methods(["GET", "POST", "PUT"])
def get_profile(request):
    """Profile endpoint"""
    if request.method == 'GET':
        # Return profile data
        return JsonResponse({
            'id': 1,
            'name': 'John Doe',
            'email': 'john@example.com',
            'bio': 'Software Developer'
        })
    
    elif request.method in ['POST', 'PUT']:
        # Handle profile updates
        try:
            data = json.loads(request.body)
            return JsonResponse({
                'message': 'Profile updated successfully',
                'data': data
            })
        except json.JSONDecodeError:
            return JsonResponse({
                'error': 'Invalid JSON'
            }, status=400)
    
    return JsonResponse({
        'error': 'Method not allowed'
    }, status=405)
