"""
How to trigger publish programmatically using pyblish api.
"""

import hou
import logging
import pyblish
from ayon_core.pipeline import registered_host
from ayon_core.pipeline.create import CreateContext

logging.basicConfig()

log = logging.getLogger("publish-from-code")
log.setLevel(logging.DEBUG)

host = registered_host()

inputs_nodes = [
    hou.node('/out/pointcacheBgeoExample').path()
]

comment = "publish from code"
context = CreateContext(host, reset=True)
log.debug("\nNodes to publish: {}\n".format(inputs_nodes))
for instance in context.instances:
    node_path = instance.data.get("instance_node")
    instance["active"] = node_path and node_path in inputs_nodes

context.save_changes()

pyblish_context = pyblish.api.Context()
pyblish_context.data["create_context"] = context
pyblish_context.data["comment"] = comment

pyblish_plugins = context.publish_plugins

error_format = "Failed {plugin.__name__}: {error} -- {error.traceback}"

for result in pyblish.util.publish_iter(pyblish_context, pyblish_plugins):
    for record in result["records"]:
        log.debug("{}: {}".format(result["plugin"].label, record.msg))

    # Exit as soon as any error occurs.
    if result["error"]:
        error_message = error_format.format(**result)
        log.debug(error_message)