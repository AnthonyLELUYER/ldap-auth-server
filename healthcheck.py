"""
Use this code to monitor the isalive of service
DO NOT UPDATE !
"""

import requests

response = requests.get("http://localhost:5000/isalive")

if response.status_code != 200:
    exit(1)
else:
    exit(0)
