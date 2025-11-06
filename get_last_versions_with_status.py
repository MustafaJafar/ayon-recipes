"""
Get Last Versions by Status and Product Name
It retrieves the last version that has a given status for the specified product name within the current folder path.
"""

import ayon_api
from ayon_core.pipeline import get_current_context
from collections import defaultdict


context = get_current_context()
project_name = context["project_name"]
folder_path = context["folder_path"]

product_name_regex = "render*"
status_name = "Approved"

folder_entity = ayon_api.get_folder_by_path(project_name, folder_path)

product_entities = ayon_api.get_products(
    project_name,
    folder_ids={folder_entity["id"]},
    product_name_regex=product_name_regex,
    fields={"id", "name", "productType"}
)

product_ids = [product["id"] for product in product_entities]

versions_by_product_id = defaultdict(list)

for entity in ayon_api.get_versions(
    project_name,
    product_ids=product_ids,
    statuses={status_name},
):
    product_id = entity["productId"]
    versions_by_product_id[product_id].append(entity)


output = {
    product_id: None
    for product_id in product_ids
}
for product_id, versions in versions_by_product_id.items():
    if not versions:
        continue
    versions.sort(key=lambda v: v["version"])
    output[product_id] = versions[-1]

print(output)