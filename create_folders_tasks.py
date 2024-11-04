from ayon_core.pipeline import get_current_project_name
from ayon_api.entity_hub import EntityHub

project_name = "my_project" # get_current_project_name()
hub = EntityHub(project_name)

for folder_name in ["asset1", "asset2"]:
    folder_entity = hub.add_new_folder(
        folder_type="Shot",  # folder type must exist in project
        name=folder_name,
        # parent_id=parent_folder_id,  # use folder id if you want a parent folder
    )

    for task_name, task_type in [
        ("modeling", "Modeling"),
        ("lookdev", "Lookdev")
    ]:
        hub.add_new_task(
            task_type=task_type,
            parent_id=folder_entity["id"],
            name=task_name,
        )
        
hub.commit_changes()