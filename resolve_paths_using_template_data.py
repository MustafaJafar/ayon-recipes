"""
Get Template data and resolve work directory template.
"""
import ayon_api
from ayon_core.pipeline import (
    Anatomy,
    get_current_context,
    get_current_host_name,
)
from ayon_core.pipeline.template_data import get_template_data
from ayon_core.lib import StringTemplate


# Get Current Context
host_name = get_current_host_name()
context = get_current_context()
project_name = context["project_name"]
folder_path = context["folder_path"]
task_name = context["task_name"]

# Get Entities
project_entity = ayon_api.get_project(project_name)
folder_entity = ayon_api.get_folder_by_path(project_name, folder_path)
task_entity = ayon_api.get_task_by_name(
    project_name, folder_entity["id"], task_name
)

# Get Template Data
template_data = get_template_data(
    project_entity, folder_entity, task_entity, host_name
)

# Add Roots to template data
anatomy = Anatomy(project_name, project_entity=project_entity)
template_data["root"] = anatomy.roots

# Resolve Path 
work_dir = anatomy.templates["work"]["default"]["directory"]
work_dir = StringTemplate.format_template(work_dir, template_data)
print(work_dir)


# -------------------------------

# Alternatively, for this particular example,
#   we already have a function to retrieve resolved work dir
from ayon_core.pipeline.workfile import get_workdir


work_dir = get_workdir(
    project_entity, folder_entity, task_entity, host_name
)

print(work_dir)