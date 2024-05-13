"""
How to trigger publisher tool actions programmatically.
"""

from ayon_core.hosts.houdini.api.lib import get_main_window
from ayon_core.tools.utils.host_tools import get_tool_by_name

def show_and_validate(publisher_window):
    publisher_window._reset_on_show = False
    publisher_window._reset_on_first_show = False
    
    
    publisher_window.make_sure_is_visible()
    
    # Reset controller
    publisher_window._controller.reset()
    
    publisher_window._on_save_clicked()
    publisher_window._on_validate_clicked()
    

comment = "Test from code"

main_window = get_main_window()
publisher_window = get_tool_by_name(
    tool_name="publisher",
    parent=main_window,
)

# Validate Only
# show_and_validate(publisher_window)

# Validate and Publish
publisher_window.show_and_publish(comment)

# Reset 
# publisher_window._controller.reset()