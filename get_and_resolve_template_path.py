"""
Get a template path from a anatomy settings in your project settings.
Get template data associated with the given task and host names.
"""

import os
import ayon_api
from ayon_core.pipeline import Anatomy
from ayon_core.pipeline.template_data import get_template_data
from ayon_core.pipeline import registered_host


# Templates to resolve
my_template_name = "work"
template_variant = "default"

# You can hardcode these values or get them from the current context inside your host.
host = registered_host()
current_context = host.get_current_context()
task_name = "cfx" or current_context["task_name"]
project_name = "Robo" or current_context["project_name"]
folder_path = "/Assets/Character/bigrobo" or current_context["folder_path"]

# get necessary data
project_entity = ayon_api.get_project(project_name)
folder_entity = ayon_api.get_folder_by_path(project_name, folder_path)
task_entity = ayon_api.get_task_by_name(
    project_name, folder_entity["id"], task_name
)

# get default anatomy data based on context
anatomy = Anatomy(project_name, project_entity=project_entity)
template_data = get_template_data(project_entity, folder_entity, task_entity, host.name)
template_data["root"] = anatomy.roots

# retrieve anatomy template my_template_name"
template = anatomy.templates[my_template_name]
template = template[template_variant]

# Let's get and resolve the directory of the template
template_dir_path = os.path.normpath(template["directory"])
print(template_dir_path)

# fill template - will fail if some data is missing
resolved_dir_path = template_dir_path.format(**template_data)
print(resolved_dir_path)