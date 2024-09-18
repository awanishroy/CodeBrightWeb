import requests
from django.conf import settings

def site_data(request):
    # API endpoint
    api_url = settings.API_URL+"/portfolio-api/all-website-data"
    
    payload = {
        "PR_WEBSITE_ID": 1
    }
    
    try:
        response = requests.post(api_url, json=payload)

        if response.status_code == 200:
            site_data = response.json()   
            return {'site_data' : site_data}
        else:
            print(f"API request failed with status code: {response.status_code}")
            return '__'
    
    except requests.RequestException as e:
        print(f"An error occurred: {e}")
        return '__'
    
def api_url(request):
    return {'api_url': settings.API_URL}