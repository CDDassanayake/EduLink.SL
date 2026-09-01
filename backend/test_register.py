import requests

# Test registration
url = "http://localhost:8000/api/v1/auth/register"
data = {
    "email": "testuser123@example.com",
    "password": "password123",
    "full_name": "Test User",
    "role": "STUDENT"
}

try:
    response = requests.post(url, json=data)
    print(f"Status: {response.status_code}")
    print(f"Response: {response.text}")
    
    if response.status_code not in [200, 201]:
        print(f"Error details: {response.json()}")
except Exception as e:
    print(f"Exception: {e}")

# Test login if registration successful
if response.status_code in [200, 201]:
    login_url = "http://localhost:8000/api/v1/auth/jwt/login"
    login_data = {
        "username": "testuser123@example.com",
        "password": "password123"
    }
    login_response = requests.post(login_url, data=login_data)
    print(f"Login Status: {login_response.status_code}")
    print(f"Login Response: {login_response.text}")
