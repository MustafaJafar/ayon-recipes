"""Get Links of a product version

When publishing workfiles, the `IntegrateInputLinksAYON` plugin automatically creates links.

This script prints the links for a specific version of a published workfile. 
It requires the **project name** and the version's **ID** from the published workfile product.

Here is a breakdown of the link directions and types:
* **`out` direction:** These links are of the type **`generative`**. This refers to the new product versions that were published from that workfile.
* **`in` direction:** These links are of the type **`reference`**. This refers to the product versions that were loaded into that workfile.
"""

import ayon_api


def get_product_version_names(project_name, version_id):
    version_data = ayon_api.get_version_by_id(project_name, version_id, {"name", "productId"})
    product_data =  ayon_api.get_product_by_id(project_name, version_data["productId"], {"name"})
    return product_data["name"], version_data["name"]

project_name = "Animal_Logic_ALab"
workfile_version_id = "5db3e83420fe11f0ac76c9dd368a2ef7"

workfile_name, workfile_version = get_product_version_names(project_name, workfile_version_id)
print(f"Find links for '{workfile_name} {workfile_version}':")

version_links = ayon_api.get_version_links(project_name, workfile_version_id)
for link in version_links:
    product, version = get_product_version_names(project_name, link["entityId"])
    print(" -", link["direction"], product, version)