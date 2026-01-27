"""
This snippet is for applying changes in settings for a project. 

The code flow is as follows: 
1. Get project settings.
2. Change the value of desired settings.
3. Set project settings.

Note:
    you can use it to modify the studio settings 
    by removing the "/{project_name}"

    To get further info about Sending Custom Requests, see 
    https://docs.ayon.dev/docs/dev_api_python/#sending-custom-requests
"""

import ayon_api
from ayon_api.utils import prepare_query_string


# Specify Addon and project name
addon_name = "core"
version = "1.6.13+dev"
project_name = "Experiments"
variant = "AYON-Dev"
site_id = None

# Prepare endpoint
query = prepare_query_string({
    "site": site_id,
    "variant": variant,
})
entrypoint = f"addons/{addon_name}/{version}/settings/{project_name}{query}"


# Get Settings
response = ayon_api.get(entrypoint)
settings = response.data

# Modify Settings
settings["publish"]["IntegrateHeroVersion"] = False

# Set Settings
# Note, here I'm using POST method.
# However, some endpoints are using PUT instead like 
#   https://docs.ayon.dev/api/#tag/Addons/operation/set_addon_site_settings
# So, it's recommended to check the API docs first.
response = ayon_api.post(
    entrypoint,
    **settings
)

print(response.detail)