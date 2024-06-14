"""
Get some info about a product in particular project in a particular folder path
 using `product_name`, `project_name` and `folder_path`
"""

import ayon_api
from ayon_core.pipeline import get_current_context


product_name = "pointcacheBgeoCache"

# Get Current Context
context = get_current_context()
project_name = context["project_name"]
folder_path = context["folder_path"]

folder_entity = ayon_api.get_folder_by_path(project_name, folder_path)

product_entities = ayon_api.get_products(
    project_name,
    folder_ids={folder_entity["id"]},
    product_name_regex=product_name,
    fields={"id", "name", "productType"}
)

for product_entity in product_entities:
    print("product_entity: ", product_entity)

version_entity = ayon_api.get_last_version_by_product_name(
    project_name,
    product_name,
    folder_entity["id"]
)

representations = ayon_api.get_representations(
    project_name,
    version_ids={version_entity["id"]},
    fields={"id", "name", "files.path"} 
)
for representation in representations:
    print("representation:", representation)
