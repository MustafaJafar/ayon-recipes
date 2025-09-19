""" Get Current Workfile IDs in the current task.

It's expected to run this script in an AYON initialized environment. e.g. from within a DCC.
"""
import ayon_api
from ayon_core.pipeline.context_tools import get_current_task_entity

task_id = get_current_task_entity({"id"})["id"]

workfiles = ayon_api.get_workfiles_info("Experiments", task_ids={task_id}, fields={"name", "id"})
for wfile in workfiles:
    print(wfile["name"], wfile["id"])