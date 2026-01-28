import os
import sys
import requests

API_URL = os.getenv("API_URL")
USERNAME = os.getenv("API_USERNAME")
PASSWORD = os.getenv("API_PASSWORD")

if not API_URL or not USERNAME or not PASSWORD:
    print("ERROR: Missing API configuration")
    sys.exit(1)

print(f"Connecting to API endpoint: {API_URL}")

try:
    response = requests.get(
        API_URL,
        auth=(USERNAME, PASSWORD),
        timeout=10,
        verify=False  # OK for labs; enable in prod
    )
except requests.RequestException as e:
    print(f"API connection failed: {e}")
    sys.exit(1)

print(f"HTTP Status Code: {response.status_code}")

if response.status_code != 200:
    print("API pre-check failed")
    sys.exit(1)

print("API pre-check successful")

