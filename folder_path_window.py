"""Select a folder path."""

from ayon_core.pipeline import get_current_project_name
from ayon_core.tools.publisher.widgets.folders_dialog import FoldersDialog
from ayon_core.tools.utils.host_tools import get_tool_by_name
from ayon_core.hosts.houdini.api.lib import get_main_window


project_name = get_current_project_name()

main_window = get_main_window()
publisher_window = get_tool_by_name( tool_name="publisher", parent=main_window)

# TODO: A dedicated Dialog should be implement using `SimpleFoldersWidget`.
#       we should avoid using `FoldersDialog` because It's highly recommend to
#         never use inner widgets of any tool...
# Note: The following dialog doesn't support changing `the project_name`
#         But, having a semi-functional dialog is better than nothing.

dialog = FoldersDialog(publisher_window.controller, main_window)
dialog.exec_()

selected_folder_path = dialog.get_selected_folder_path()

print ("asset name:", selected_folder_path)
