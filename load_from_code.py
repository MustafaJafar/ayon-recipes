"""
Load representations from code.
This script first retrieve the representation context which is expected by the loader plugins.
Then get loader plugin by name (class name) and load.
"""
import ayon_api
from ayon_core.pipeline.load import (
    get_loaders_by_name,
    load_with_repre_context,
    get_representation_context
)

def get_representation(project_name, folder_path, product_name, version, representation_name):

    folder_entity = ayon_api.get_folder_by_path(
        project_name, folder_path, fields={"id"}
    )

    product_entity = ayon_api.get_product_by_name(
        project_name,
        product_name=product_name,
        folder_id=folder_entity["id"],
        fields={"id"},
    )
    
    if version in {"hero", "latest"}:
 
        hero = version == "hero"
        latest = version == "latest"
        versions = ayon_api.get_versions(
            project_name,
            product_ids={product_entity["id"]},
            fields={"id"},
            hero=hero,
            latest=latest
        )
        version_entity = list(versions)[-1]
    else:
        version_entity = ayon_api.get_version_by_name(
                project_name, version, product_id=product_entity["id"], fields={"id"}
            )

    representation_entity = ayon_api.get_representation_by_name(
            project_name,
            representation_name,
            version_id=version_entity["id"],
            # fields={"files", "context"},
        )
    
    # path = get_filepath_from_representation_entity(representation_entity)
    
    return get_representation_context(project_name, representation_entity)

def load_representation(loader_name, representation_context, loader_args=None):
    loader = get_loaders_by_name().get(loader_name)

    container = load_with_repre_context(
        loader,
        representation_context,
        options=loader_args
    )

    return container


project_name = "Experiments"
folder_path = "/things/usd_assets"
product_name = "usdAsset"
version = "latest" # can be a version number or "latest" or "hero"
representation_name = "usd"

loader_name = "USDReferenceLoader"

representation = get_representation(project_name, folder_path, product_name, version, representation_name)
container = load_representation(loader_name, representation)

print(container)