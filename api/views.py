"""
API views for the profile endpoint.
"""
import logging
import requests
from datetime import datetime
from django.http import JsonResponse
from django.views.decorators.http import require_GET

logger = logging.getLogger(__name__)

CAT_FACTS_API_URL = "https://catfact.ninja/fact"

@require_GET
def api_root(request):
    """Root endpoint for quick sanity check."""
    return JsonResponse({
        "message": "Welcome to Tochukwu Ihejirika’s Profile API",
        "endpoints": {
            "profile": "/me/"
        },
        "timestamp": datetime.utcnow().isoformat() + "Z"
    })


@require_GET
def get_profile(request):
    """
    Returns personal profile information and a dynamic cat fact.
    """
    try:
        # Fetch random cat fact
        response = requests.get(CAT_FACTS_API_URL, timeout=5)
        cat_fact = response.json().get("fact", "Cats are awesome!")
    except Exception as e:
        logger.error(f"Error fetching cat fact: {e}")
        cat_fact = "Could not fetch cat fact right now."

    # Build your profile response
    profile_data = {
        "full_name": "Tochukwu Ihejirika",
        "github_handle": "@tochukwu-ihejirika",
        "linkedin": "https://linkedin.com/in/tochukwu-ihejirika",
        "role": "Backend Developer | FastAPI" ,
        "email": "tochukwuihejirika@gmail.com.com",
        "skills": ["Python", "REST APIs", "JavaScript", "React", "SQL"],
        "current_time": datetime.utcnow().isoformat() + "Z",
        "fun_fact": cat_fact,
    }

    return JsonResponse(profile_data)
