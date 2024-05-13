"""
Get Settings and addon info associated with the bundle in your running ayon session.
"""
import ayon_api
import os 


if ayon_api.is_connection_created():
    con = ayon_api.get_server_api_connection()

    # Bundle Settings
    bundle_name = os.getenv("AYON_BUNDLE_NAME")
    bundle_settings = con.get_addons_settings(bundle_name)
    print(bundle_settings["houdini"]["publish"]["CollectFilesForCleaningUp"])

    # Addons Info (name, title, version, ...)
    print(con.get_addons_info())