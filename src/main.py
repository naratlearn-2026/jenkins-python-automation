import os
import sys
import platform

print("Python automation started")
print(f"Python version: {platform.python_version()}")

# Read credentials from environment
username = os.getenv("API_USERNAME")
password = os.getenv("API_PASSWORD")

if not username or not password:
    print("ERROR: Credentials not found")
    sys.exit(1)

# NEVER print real passwords in real pipelines
print(f"Credentials received for user: {username}")

# Simulated validation logic
value = 10
if value < 5:
    print("Validation failed")
    sys.exit(1)

print("Validation passed")

