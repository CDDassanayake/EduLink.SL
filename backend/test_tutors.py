import requests
import traceback

# Test tutors API
base_url = "http://localhost:8000/api/v1"

# Test search tutors
print("Testing GET /tutors...")
try:
    response = requests.get(f"{base_url}/tutors")
    print(f"Status: {response.status_code}")
    print(f"Response: {response.text}")
except Exception as e:
    print(f"Error: {e}")
    traceback.print_exc()
print()

# Test get tutor profile (using a random UUID for testing)
print("Testing GET /tutors/{id}/profile...")
test_id = "00000000-0000-0000-0000-000000000000"
try:
    response = requests.get(f"{base_url}/tutors/{test_id}/profile")
    print(f"Status: {response.status_code}")
    print(f"Response: {response.text}")
except Exception as e:
    print(f"Error: {e}")
    traceback.print_exc()
print()

# Test get tutor availability
print("Testing GET /tutors/{id}/availability...")
try:
    response = requests.get(f"{base_url}/tutors/{test_id}/availability")
    print(f"Status: {response.status_code}")
    print(f"Response: {response.text}")
except Exception as e:
    print(f"Error: {e}")
    traceback.print_exc()
