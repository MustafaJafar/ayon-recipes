"""
This was made for learning about writing custom rest commands.
However, it's recommended to use ayon_api.
"""

import os
import httpx


class SimpleAyonRestCommands:
    def __init__(self, ayon_server_url, username, password):
        self.ayon_server_url = ayon_server_url
        self.credentials = {
            "name": username,
            "password":password
        }
        self.headers = {}
        self.ayon_login()
        
    def ayon_login(self):
        req = f"{self.ayon_server_url}/api/auth/login"
        response = httpx.post(
            req,
            json=self.credentials,
        )
        self.token = response.json().get("token")
        self.headers["Authorization"] = f"Bearer {self.token}"

    def get_projects(self):
        req = f"{self.ayon_server_url}/api/projects"
        response = httpx.get(
            req,
            headers=self.headers
        )
        return response.json().get("projects")
    
    def get_bundles(self):
        req = f"{self.ayon_server_url}/api/bundles"
        response = httpx.get(
            req,
            params={
              "archived": False  
            },
            headers=self.headers
        )
        return response.json()
        
    def get_addons(self):
        req = f"{self.ayon_server_url}/api/addons"
        response = httpx.get(
            req,
            headers=self.headers
        )
        return response.json()

    def delete_addon_version(self, addon_name, addon_version): 
        req = f"{self.ayon_server_url}/api/addons/{addon_name}/{addon_version}"
        response = httpx.delete(
            req,
            params={
                "purge" : True
            },
            headers=self.headers
        )
        return response.json()
    
    def upload_addon_zip_url(self, addon_url, addon_name, addon_version):
        req = f"{self.ayon_server_url}/api/addons/install"
        response = httpx.post(
            req,
            params = {
                "url" : addon_url,
                "addonName": addon_name,
                "addonVersion" :addon_version
            },
            headers=self.headers
        )
        return response.json()

    def upload_addon_zip_file(self, addon_filepath):
        chunk_size = 1024 * 1024
        req = f"{self.ayon_server_url}/api/addons/install"
         
        with open(addon_filepath, "rb") as stream:
            response =  httpx.post(
                req, 
                data=self.upload_chunks_iter(stream, chunk_size),
                headers=self.headers
            )
        response.raise_for_status() 
        return response.json()

    @staticmethod
    def upload_chunks_iter(file_stream, chunk_size):
        while True:
            chunk = file_stream.read(chunk_size)
            if not chunk:
                break
            yield chunk
    

if __name__ == "__main__":
    # get ayon server credentials
    username =  "admin"
    password = "admin"
    ayon_server_url = "http://192.168.1.4:5000"
    addon_path = "E:/Ynput/ayon-core/server_addon/packages/houdini-0.2.13.zip"

    my_ayon = SimpleAyonRestCommands(ayon_server_url, 
                                     username,
                                     password)

    file_name = os.path.basename(addon_path).rstrip(".zip")
    addon_name, addon_version = file_name.split("-", 1)
    ## Delete and addon by version
    print("Delete addon: {}, version: {}".format(addon_name, addon_version))
    my_ayon.delete_addon_version(addon_name, addon_version)
    

    # Upload Addon from file on disk 
    print("Upload addon: {}, version: {}".format(addon_name, addon_version))
    res = my_ayon.upload_addon_zip_file(addon_path) 
    print (res)
