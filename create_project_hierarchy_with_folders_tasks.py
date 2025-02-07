import re
import ayon_api
from ayon_api.entity_hub import EntityHub
from ayon_core.pipeline import get_current_project_name


def format_label(asset_name):
    # Replace underscores with spaces and
    #  capitalize the first letter of each word.
    
    label = asset_name.replace("_", " ").title()
    label = re.sub(r'(\D)(\d+)$', r'\1 \2', label)
    return label


tasks = {
    # task_type: task_name,
    "Modeling": "modeling",
    "Lookdev": "lookdev",
}

project_name = "my_project" # get_current_project_name()
ayon_hub = EntityHub(project_name)

project_folders = ayon_api.get_folders(project_name, folder_types={"Asset"}, fields={"name"})
project_folders = [f["name"] for f in project_folders]

asset_names = [f"asset_{i}" for i in range(1, 101)]

parent_folder_name = "my_assets"
parent_folder = ayon_api.get_folder_by_path(project_name, parent_folder_name, fields={"id"})
if parent_folder is None:
    parent_folder = ayon_hub.add_new_folder(
        folder_type="Folder",
        name=parent_folder_name,
        label=format_label(parent_folder_name),
    )
    ayon_hub.commit_changes()

for asset_name in asset_names:  
    if asset_name not in project_folders:
        # Create a new entity hub to clear the cache.
        ayon_hub = EntityHub(project_name)

        folder_entity = ayon_hub.add_new_folder(
            folder_type="Asset",
            name=asset_name,
            label=format_label(asset_name),
            parent_id=parent_folder["id"]
        )
        
        for task_type, task_name in tasks.items():
            task_entity = ayon_hub.add_new_task(
                    task_type=task_type,
                    name=task_name,
                    label=task_type,
                    parent_id=folder_entity["id"],
                )
        ayon_hub.commit_changes()
