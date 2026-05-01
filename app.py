import requests

url = "https://api-call-tracker-production.up.railway.app/track"

params = {
    'userId': 'user_001',
    'projectId': 'proj_alpha',
    'idname': 'cl'
}

# Send GET request
response = requests.get(url, params=params)

# Check response
print(f"Status Code: {response.status_code}")
print(f"Response: {response.text}")