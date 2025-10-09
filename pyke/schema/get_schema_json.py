import json

import requests

url = "http://www.mingweisamuel.com/riotapi-schema/openapi-3.0.0.json"

response = requests.get(url)

code = response.status_code

if code == 200:
    json_content = response.json()

    with open("./pyke/schema/schema.json", "w") as f:
        json.dump(json_content, f, indent=4)
else:
    print(f"Error: {code}")
    quit()
