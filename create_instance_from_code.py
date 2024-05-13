"""
Create ayon instances from code.
"""

import ayon_api
from ayon_core.pipeline import registered_host
from ayon_core.pipeline.create import CreateContext


host = registered_host()

creator_identifier = "io.openpype.creators.houdini.pointcache"

# You can hardcode these values or get them from the current context inside your host.
current_context = host.get_current_context()
task_name = "cfx" or current_context["task_name"]
project_name = "Robo" or current_context["project_name"]
folder_path = "/Assets/Character/bigrobo" or current_context["folder_path"]
variant = "MyExampleVariant"

folder_entity = ayon_api.get_folder_by_path(
    project_name, folder_path, fields={"id"}
)


create_context = CreateContext(host)
create_context.create(
    creator_identifier,
    variant=variant,
    folder_entity=ayon_api.get_folder_by_path(project_name, folder_path),
    task_entity=ayon_api.get_task_by_name(project_name, folder_entity["id"], task_name),
    pre_create_data={"use_selection": True}  # creator options
)