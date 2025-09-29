"""
Get Template data and resolve work directory template.
"""
from ayon_core.lib import StringTemplate
from ayon_core.pipeline import Anatomy
from ayon_core.pipeline.template_data import get_template_data
from ayon_core.pipeline.context_tools import (
    get_current_project_entity,
    get_current_folder_entity,
    get_current_task_entity,
    get_current_host_name
)

from ayon_core.pipeline.workfile import get_workdir


# Get Current host name
host_name = get_current_host_name()

# Get Entities
project_entity = get_current_project_entity()
folder_entity = get_current_folder_entity()
task_entity = get_current_task_entity()

# Get Template Data
template_data = get_template_data(
    project_entity, folder_entity, task_entity, host_name
)

# Add Roots to template data
anatomy = Anatomy()
template_data["root"] = anatomy.roots

# Resolve Path 
work_dir = anatomy.templates["work"]["default"]["directory"]
work_dir = StringTemplate.format_template(work_dir, template_data)
print(work_dir)

# -------------------------------

# Alternatively, for this particular example,
#   we already have a function to retrieve resolved work dir

work_dir = get_workdir(
    project_entity, folder_entity, task_entity, host_name
)

print(work_dir)