"""Using the AYON Python API

When using the **AYON Python API** from within an AYON-initialized environment, you don't have to log in.
In contrast, when using the API from a standalone application, you may need to log in first or set specific environment variables.

This script shows different ways to login to ayon python api.
"""

import os
import ayon_api

# [easiest way] Using a service account api key.

ayon_url = "http://localhost:5000"
ayon_service_api_key = "veryinsecureapikey"

os.environ["AYON_SERVER_URL"] = ayon_url
os.environ["AYON_API_KEY"] = ayon_service_api_key

ayon = ayon_api.get_server_api_connection()

user = ayon.get_user()
print(f"Logged in as user \"{user['name']}\"")
ayon_api.close_connection()

"""Expected Output
>>> Logged in as user "service"
"""

# Using an authentication bearer token.
ayon_url = "http://localhost:5000"
auth_key = ayon_api.login_to_server(  # get an auth key.
    url=ayon_url,
    username="admin",
    password="ayon"
)

os.environ["AYON_SERVER_URL"] = ayon_url
os.environ["AYON_API_KEY"] = auth_key

ayon = ayon_api.get_server_api_connection()

user = ayon.get_user()
print(f"Logged in as user \"{user['name']}\"")
ayon_api.close_connection()

"""Expected Output
>>> Logged in as user "Admin"
"""

# Using a service account to initiate the connection.
# Then login using username and password.

AYON_SERVER_URL = "http://localhost:5000"
AYON_API_KEY = "veryinsecureapikey"

os.environ["AYON_SERVER_URL"] = AYON_SERVER_URL
os.environ["AYON_API_KEY"] = AYON_API_KEY

ayon = ayon_api.get_server_api_connection()
ayon.login("admin", "ayon")  # (username, password)

user = ayon.get_user()
print(f"Logged in as user \"{user['name']}\"")
ayon_api.close_connection()

"""Expected Output
>>> Logged in as user "Admin"
"""