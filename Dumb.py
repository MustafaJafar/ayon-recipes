"""
Empty Pyblish plugin that used for inspection.

Note: 
    PLugin's order is an int constant.
    Current Orders:
        pyblish.api.CollectorOrder == 0
        pyblish.api.ValidatorOrder == 1
        pyblish.api.ExtractorOrder == 2
        pyblish.api.IntegratorOrder == 3


    Sometimes, you can add some number to the order
      to adjust its order.
    You may want to adjust the order to make it run
      after a particular plugin.
"""

import pyblish.api
import hou


class Dumb(pyblish.api.InstancePlugin):
    """Dumb

    """

    order = pyblish.api.CollectorOrder + 0.5
    hosts = ["houdini"]
    label = "Dumb"

    def process(self, instance):

       self.log.debug(instance.data)
