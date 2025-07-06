# Paul Fralix, 07/06/2025, Assignment 9.2
# This code is a standalone script that retrieves data from the Open Notify API
# and prints the JSON response. It is not a test script but a functionality script.

import requests

response = requests.get("http://api.open-notify.org/astros.json")
print(response.status_code)         # Expect 200
print(response.json())              # View JSON response


