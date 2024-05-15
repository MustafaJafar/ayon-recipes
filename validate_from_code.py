"""
How to run validation plugins programmatically using pyblish api.
"""

import logging
import pyblish
from ayon_core.pipeline import registered_host
from ayon_core.pipeline.create import CreateContext

host = registered_host()

assert host, "No registered host."

logging.basicConfig()
log = logging.getLogger("publish-from-code")
log.setLevel(logging.DEBUG)
    
create_context = CreateContext(host)

# # filter instances based on some condition
# for instance in create_context.instances:
#     if (some condition):
#         instance["active"] = False
#     instance["active"] = True
# context.save_changes()

pyblish_context = pyblish.api.Context()
pyblish_context.data["create_context"] = create_context
pyblish_plugins = create_context.publish_plugins

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