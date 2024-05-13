"""
How to run validation plugins programmatically using pyblish api.
"""

import hou
import logging
import pyblish.util
from ayon_core.pipeline import registered_host
from ayon_core.pipeline.create import CreateContext

logging.basicConfig()

log = logging.getLogger("validate-from-code")
log.setLevel(logging.DEBUG)

all_input_nodes = [
    hou.node('/out/reviewMain'),
    hou.node('/out/S_BigRoboMain')
]

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
pyblish_plugins = context.publish_plugins

# Silent Run collect and validate order of pyblish plugins
pyblish_context = pyblish.util.collect(pyblish_context, pyblish_plugins)
# pyblish_context = pyblish.util.validate(pyblish_context, publish_plugins)

# Run validations one by one
error_format = "Failed {plugin.__name__}: {error} -- {error.traceback}"

for result in pyblish.util.validate_iter(pyblish_context, pyblish_plugins):
    for record in result["records"]:
        log.debug("{}: {}".format(result["plugin"].label, record.msg))

    # Exit as soon as any error occurs.
    if result["error"]:
        error_message = error_format.format(**result)
        log.debug(error_message)