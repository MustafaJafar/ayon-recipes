"""
Upload addon to AYON.
"""

import os
import logging
import ayon_api


logging.basicConfig(level=logging.INFO)
log = logging.getLogger("upload_package")

trigger_restart = True

os.environ["AYON_SERVER_URL"] = "ayon-url"  # e.g. "http://127.0.0.1:5000/"
os.environ["AYON_API_KEY"] = "service-user-key"
ayon_api.init_service()

addon_path = "<some-path>/<some-addon>-<some-version>.zip"  # e.g. 'C:/ayon-core/package/core-0.3.1-dev.1.zip'
log.info("Uploading: '{}'".format(addon_path))
response = ayon_api.upload_addon_zip(addon_path)
    
if trigger_restart: 
    server = ayon_api.get_server_api_connection()
    if server:
        server.trigger_server_restart()