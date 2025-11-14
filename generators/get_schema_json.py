import json

import requests

url = "https://www.mingweisamuel.com/riotapi-schema/openapi-3.0.0.json"

response = requests.get(url, timeout=10)

if response.status_code == 200:
    json_content = response.json()

    with open("./pyke/generators/schema.json", "w") as f:
        json.dump(json_content, f, indent=4)
else:
    print(f"Error: {response.status_code}")
    quit()
