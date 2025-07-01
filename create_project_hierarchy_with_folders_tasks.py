""" Create Project Hierarchy with Folders and Tasks.

This example code creates a project hierarchy with a list of assets and tasks if they don't already exist.

Created hierarchy:
```
{project_name}
    └── My Assets
            ├── Asset 1 
            |     ├── Modeling
            |     └── Lookdev
            ├── .
            ├── .
            └── Asset_100
                ├── Modeling
                └── Lookdev
```

Note 1: You'll always have access to the IDs of the entities in the mentioned project structure. If an entity is queried and doesn't exist, it will be created.

Note 2: 
    This code doesn't create a project if it doesn't already exist.
    All folder and task types MUST exist before running this script.
"""

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


project_name = "my_project" # get_current_project_name()
asset_to_create = [f"asset_{i}" for i in range(1, 101)]
tasks_to_create = {
    # task_name: task_type,
    "modeling": "Modeling",
    "lookdev": "Lookdev",
}

# Get or create Parent Folder
parent_folder_name = "my_assets"
parent_folder = ayon_api.get_folder_by_path(project_name, parent_folder_name, fields={"id"})
if parent_folder is None:
    ayon_hub = EntityHub(project_name)
    parent_folder = ayon_hub.add_new_folder(
        folder_type="Folder",
        name=parent_folder_name,
        label=format_label(parent_folder_name),
    )
    ayon_hub.commit_changes()

# Get all asset entities
asset_entities = ayon_api.get_folders(project_name, folder_types={"Asset"}, fields={"name", "id", "path"})
asset_entities = {f["name"]: f for f in asset_entities}
for asset_name in asset_to_create:

    ayon_hub = EntityHub(project_name)
    # Get or create asset
    if asset_name in asset_entities: 
        asset_entity = asset_entities[asset_name]
    else:
        asset_entity = ayon_hub.add_new_folder(
            folder_type="Asset",
            name=asset_name,
            label=format_label(asset_name),
            parent_id=parent_folder["id"]
        )
    print(asset_name,":", asset_entity["id"])

    # Get or create tasks
    task_entities = ayon_api.get_tasks(project_name, folder_ids={asset_entity["id"]}, fields={"name", "id"})
    task_entities = {t["name"]:t for t in task_entities}
    for task_name, task_type in tasks_to_create.items():
        if task_name in task_entities:
            task_entity = task_entities[task_name]
        else:
            task_entity = ayon_hub.add_new_task(
                    task_type=task_type,
                    name=task_name,
                    label=format_label(task_name),
                    parent_id=asset_entity["id"],
                )
        print(" ", task_name,":", task_entity["id"])
    ayon_hub.commit_changes()
