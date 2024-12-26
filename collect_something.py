import pyblish.api
from ayon_core.lib import BoolDef
from ayon_core.pipeline import publish


class CollectSomeInstanceAttrs(pyblish.api.InstancePlugin,
                               publish.AYONPyblishPluginMixin,):
    """A boilerplate to add an attrdef to publish instances."""

    label = "Collect Some Instance Attrs"
    order = pyblish.api.CollectorOrder
    hosts = ["traypublisher"]
    families = ["*"]

    def process(self, instance):
        # do something
        pass

    @classmethod
    def get_attribute_defs(cls):
        return [
            BoolDef(
                "a_toggle_instance",
                default=True,
                label="A Toggle per instance"
            )
        ]


class CollectSomeContextAttrs(pyblish.api.ContextPlugin,
                               publish.AYONPyblishPluginMixin,):
    """A boilerplate to add an attrdef to publish context."""

    label = "Collect Some Context Attrs"
    order = pyblish.api.CollectorOrder
    hosts = ["traypublisher"]

    def process(self, context):
        # do something
        pass

    @classmethod
    def get_attribute_defs(cls):
        return [
            BoolDef(
                "a_toggle_context",
                default=True,
                label="A Toggle per context"
            )
        ]
