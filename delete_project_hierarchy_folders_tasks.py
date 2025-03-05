from ayon_api.operations import OperationsSession
from ayon_api import get_products, get_tasks, get_folders
session = OperationsSession()

PROJECT_NAME = "<PROJECTNAME>"
INPUT_IDS = [
    "<FOLDER_ID_01>",
    "<FOLDER_ID_02>",
]

folders_to_remove = [
    f
    for f in get_folders(
        PROJECT_NAME,
        fields=["id", "parentId", "name", "folderType"],
    )
    if f["id"] in INPUT_IDS or f["parentId"] in INPUT_IDS
]
folders_ids_to_remove = [folder["id"] for folder in folders_to_remove]

products_to_remove = [
    p
    for p in get_products(
        PROJECT_NAME, folder_ids=folders_ids_to_remove, fields=["id", "name"]
    )
]
tasks_to_remove = [
    t
    for t in get_tasks(
        PROJECT_NAME, folder_ids=folders_ids_to_remove, fields=["id", "name"]
    )
]

for task in tasks_to_remove:
    print("Deleted task", task["name"])
    session.delete_entity(PROJECT_NAME, "task", task["id"])
session.commit()

for product in products_to_remove:
    print(f"Deleted product {product['name']}")
    session.delete_entity(PROJECT_NAME, "product", product["id"])
session.commit()

for folder in folders_to_remove:
    print("Deleted folder", folder["name"])
    session.delete_entity(PROJECT_NAME, "folder", folder["id"])
session.commit()