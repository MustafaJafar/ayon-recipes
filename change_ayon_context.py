import ayon_api
from ayon_core.pipeline.context_tools import (
    change_current_context,
    get_current_project_name
)


project_name = get_current_project_name()  # "Animal_Logic_ALab" 
folder_path = "/assets/book_encyclopedia01"
# task_name = "modeling" 
task_name = "lookdev"

folder_entity = ayon_api.get_folder_by_path(project_name, folder_path)
task_entity = ayon_api.get_task_by_folder_path(project_name, folder_path, task_name)

folder_entity = ayon_api.get_folder_by_path(project_name, folder_path)
task_entity = ayon_api.get_task_by_folder_path(project_name, folder_path, task_name)

changed = change_current_context(
    folder_entity,
    task_entity
)