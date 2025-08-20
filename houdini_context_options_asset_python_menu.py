"""**Houdini Python Context Menu**

When you create a **Python** menu in your **Houdini** context options editor with the following snippet, 
it will generate a list of all assets in your current project. The list will display the asset name, 
but its value will be the corresponding asset's folder path. 
In the **folder path parameter** of any of the **AYON HDA** loaders, you can use the value of a context option with @option_name.

"""

import ayon_api
from ayon_core.pipeline import get_current_project_name

project_name = get_current_project_name()
asset_entities = ayon_api.get_folders(project_name, folder_types={"Asset"}, fields={"id", "name", "path",})
asset_list = [(f["name"], f["path"]) for f in asset_entities]

return asset_list