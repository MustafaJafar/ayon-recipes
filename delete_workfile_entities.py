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