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
def get_profile(request):
    """
    Returns user profile info with a random cat fact.
    Matches HNG task JSON structure requirements.
    """
    try:
        # Fetch random cat fact
        response = requests.get(CAT_FACTS_API_URL, timeout=5)
        cat_fact_data = response.json()
        cat_fact = cat_fact_data.get("fact", "Cats are fascinating creatures.")
    except Exception as e:
        logger.error(f"Error fetching cat fact: {e}")
        cat_fact = "Unable to fetch cat fact right now."

    data = {
        "status": "success",
        "user": {
            "name": "Tochukwu Ihejirika",
            "email": "tochukwu.ihejirika@example.com",
            "stack": "Backend Developer | Django & API Specialist"
        },
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "fact": cat_fact
    }

    return JsonResponse(data)
