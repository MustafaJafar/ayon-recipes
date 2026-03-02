import ayon_api
from ayon_api.server_api import RequestTypes
from ayon_core.lib import get_media_mime_type

project_name = "AY_CG_demo"
endpoint_url = f"projects/{project_name}/files"
filename = "some_random_file.png"
file_path  =  rf"E:\Ynput\tmp\{filename}"

ayon_con = ayon_api.get_server_api_connection()
content_type = get_media_mime_type(file_path)
headers = ayon_con.get_headers(content_type)
headers["x-file-name"] = filename

output = ayon_con.upload_file(
    endpoint_url,
    file_path,
    headers=headers,
    request_type=RequestTypes.post,
)

print(output)  # <Response [201]>