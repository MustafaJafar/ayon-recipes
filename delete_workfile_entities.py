from ayon_api import get_workfiles_info
from ayon_api.operations import OperationsSession

project_name = "Animal_Logic_ALab"

workfile_ids = [
    "a314146869c84160b88c944230a95bd2",
    "d87033db1a9e496a8a34597d63471a6c",
    "7cd2c180882541e88fe2d64d08918885",
]

session = OperationsSession()
for workfile_id in workfile_ids:
    session.delete_entity(project_name, "workfile", workfile_id)
session.commit()


# Alternatively, you can delete workfiles below a task.
task_id = "1046af8120e911f0ba9f59f45369a101"
workfiles_info = get_workfiles_info(project_name, task_ids=[task_id])
ayon_session = OperationsSession()
for workfile_info in workfiles_info:
    if ... :  # Use a condition to tell which one to delete or which one to keep.
        continue
    ayon_session.delete_entity(project_name, "workfile", workfile_info["id"])
ayon_session.commit()