"""
How to trigger publish programmatically using pyblish api.
"""

import hou
import logging
import pyblish.util
from ayon_core.pipeline import registered_host
from ayon_core.pipeline.create import CreateContext

logging.basicConfig()

log = logging.getLogger("publish-from-code")
log.setLevel(logging.DEBUG)

all_input_nodes = [
    hou.node('/out/reviewMain'),
    hou.node('/out/S_BigRoboMain')
]

comment = "publish from code"

all_input_subsets = [n.evalParm("subset") for n in all_input_nodes]

host = registered_host()
context = CreateContext(host, reset=True)

for instance in context.instances:
    if instance.get("subset") not in all_input_subsets:
        instance["active"] = False
        instance.data["publish"] = False
        continue

    # make sure the instance is active
    instance["active"] = True

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