import os
import json
import ayon_api


AYON_SERVER_URL = "http://localhost:5000"
AYON_API_KEY = "veryinsecureapikey"

os.environ["AYON_SERVER_URL"] = AYON_SERVER_URL
os.environ["AYON_API_KEY"] = AYON_API_KEY

ayon = ayon_api.get_server_api_connection()

for i in range(100):
    user_name = f"demouser{i:0>2}"

    file_name = os.path.join("users", f"{user_name}")
    if not os.path.isfile(f"{file_name}.json"):
        continue

    with open(f"{file_name}.json") as f:
        user_data = json.load(f)
        user_data["attrib"].pop("avatarUrl")
        user_data["data"] = {"defaultAccessGroups": ["artist"]}
        user_data["password"] = "ayon"
        ayon.put(
            f"users/{user_name}",
            **user_data
        )
        print(f"User '{user_name}' is created.")

    with open(f"{file_name}.jpg", "rb") as f:
        ayon.raw_put(
            f"users/{user_name}/avatar",
            data=f.read(),
            headers={"Content-Type": "image/jpeg"},
        )
        print(f"Avatar for '{user_name}' is uploaded.")