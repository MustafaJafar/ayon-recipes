"""
Create a link between every version entity loaded in
the scene to current workfile directory.

This script assumes you have added the following link type
in your project anatomy:
```
{
    "style": "solid",
    "link_type": "loaded_versions",
    "input_type": "version",
    "output_type": "workfile",
    "color": "#ff6d1f"
}
```

"""

import os
from collections import defaultdict

import ayon_api
from ayon_api.graphql import GraphQlQuery

from ayon_core.pipeline import registered_host
from ayon_core.pipeline.context_tools import (
    get_current_project_name,
    get_current_task_entity,
)


def get_workfiles_in_task(project_name: str, task_id: str) -> bool:

    query = GraphQlQuery("Workfiles")
    project_name_var = query.add_variable(
        "projectName", "String!", project_name
    )
    task_id_var = query.add_variable(
        "taskId", "String!", task_id
    )
    project_query = query.add_field("project")
    project_query.set_filter("name", project_name_var)
    task_query = project_query.add_field("task")
    task_query.set_filter("id", task_id_var)
    workfiles_query = task_query.add_field("workfiles")
    edges_query = workfiles_query.add_field("edges")
    node_query = edges_query.add_field("node")
    node_query.add_field("id")
    node_query.add_field("name")

    parsed_data = query.query(ayon_api.get_server_api_connection())
    workfiles = {}
    for node in (
        parsed_data["project"]["task"]["workfiles"]["edges"]
    ):
        workfiles[node["node"]["name"]] = node["node"]["id"]
    
    return workfiles


def get_workfile_id_by_name(project_name, task_id, workfile_name):
    workfiles = get_workfiles_in_task(project_name, task_id)
    return workfiles[workfile_name]


def get_loaded_versions_ids(host):

    representation_id_to_containers = defaultdict(list)
    for container in host.get_containers():
        representation_id: str = container["representation"]
        representation_id_to_containers[representation_id].append(container)

    # Get all generative input links for the loaded product versions
    representation_entities = list(ayon_api.get_representations(
        host.get_current_project_name(),
        representation_ids=set(representation_id_to_containers.keys()),
        fields={"versionId"}
    ))
    scene_version_ids = {repre["versionId"] for repre in representation_entities}
    return scene_version_ids


host = registered_host()
current_workfile = host.get_current_workfile()
workfile_name = os.path.basename(current_workfile)

task_id = get_current_task_entity({"id"})["id"]


project_name = get_current_project_name()
link_type = "loaded_versions"
workfile_id = get_workfile_id_by_name(project_name, task_id, workfile_name)

versions_ids = get_loaded_versions_ids(host)

for version_id in versions_ids:
    # TODO: Don't create a link if it exists already.
    ayon_api.create_link(
        project_name,
        link_type,
        version_id,
        "version",
        workfile_id,
        "workfile"
    )


## ------------ Test ------------ ##
# Currently, I check the links in pgAdmin.
# TODO: Write some code to list linked versions.