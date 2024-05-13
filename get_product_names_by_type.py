"""
Get products of specified type published to a particular folder_path within a particular project_name.
"""

import ayon_api
from ayon_core.pipeline import registered_host


# You can hardcode these values or get them from the current context inside your host.
host = registered_host()
current_context = host.get_current_context()
project_name = "Robo" or current_context["project_name"]
folder_path = "/Assets/Character/bigrobo" or current_context["folder_path"]

my_product_type = "usd"


id_only = ["id"]
folder_entity = ayon_api.get_folder_by_path(project_name,
                                            folder_path,
                                            fields=id_only)
my_folder_id = folder_entity["id"]

my_usd_products = ayon_api.get_products(
    project_name,
    folder_ids = [my_folder_id],
    product_types = [my_product_type]
    
)

print([product["name"] for product in my_usd_products])
