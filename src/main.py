import sys
import platform

print("Python automation started")
print(f"Python version: {platform.python_version()}")

# Simulate a validation check
value = 10
if value < 5:
    print("Validation failed")
    sys.exit(1)

print("Validation passed")
