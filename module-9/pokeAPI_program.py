import requests

response = requests.get("http://pokeapi.co/api/v2/generation/?limit=2")
print(response.status_code)  # Expect 200
      
print(response.json())       # View JSON response

import json
def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

jprint(response.json())  # Pretty print JSON response
