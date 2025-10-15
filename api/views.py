"""
API views for the profile endpoint.
"""
import logging
from datetime import datetime
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
import requests

logger = logging.getLogger(__name__)

# Configuration
CAT_FACTS_API_URL = "https://catfact.ninja/fact"
API_TIMEOUT = 5  # seconds
FALLBACK_FACT = "Cats are amazing creatures!"

# Personal information - UPDATE THESE WITH YOUR DETAILS
USER_INFO = {
    "email": "tochukwuihejirika3@gmail.com",  # CHANGE THIS
    "name": "Tochukwu Ihejirika",  # CHANGE THIS
    "stack": "Python/Django"  # CHANGE THIS if needed
}


def fetch_cat_fact():
    """
    Fetch a random cat fact from the Cat Facts API.
    
    Returns:
        str: A cat fact or fallback message if API fails
    """
    try:
        logger.info(f"Fetching cat fact from {CAT_FACTS_API_URL}")
        response = requests.get(CAT_FACTS_API_URL, timeout=API_TIMEOUT)
        response.raise_for_status()
        
        data = response.json()
        fact = data.get('fact', FALLBACK_FACT)
        logger.info("Successfully fetched cat fact")
        return fact
        
    except requests.exceptions.Timeout:
        logger.error("Cat Facts API request timed out")
        return FALLBACK_FACT
        
    except requests.exceptions.RequestException as e:
        logger.error(f"Failed to fetch cat fact: {str(e)}")
        return FALLBACK_FACT
        
    except (KeyError, ValueError) as e:
        logger.error(f"Failed to parse cat fact response: {str(e)}")
        return FALLBACK_FACT


@csrf_exempt
@require_http_methods(["GET"])
def get_profile(request):
    """
    GET /me endpoint that returns profile information with a dynamic cat fact.
    
    Returns:
        JsonResponse: Profile data with current timestamp and cat fact
    """
    try:
        # Get current UTC timestamp in ISO 8601 format
        current_time = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3] + 'Z'
        
        # Fetch a fresh cat fact
        cat_fact = fetch_cat_fact()
        
        # Construct response
        response_data = {
            "status": "success",
            "user": {
                "email": USER_INFO["email"],
                "name": USER_INFO["name"],
                "stack": USER_INFO["stack"]
            },
            "timestamp": current_time,
            "fact": cat_fact
        }
        
        logger.info(f"Successfully processed /me request at {current_time}")
        
        return JsonResponse(
            response_data,
            status=200,
            content_type='application/json'
        )
        
    except Exception as e:
        logger.error(f"Unexpected error in get_profile: {str(e)}")
        return JsonResponse(
            {
                "status": "error",
                "message": "An unexpected error occurred"
            },
            status=500,
            content_type='application/json'
        )