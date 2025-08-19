"""
Accessing the USD Resolver Manually to Resolve a URI Path

This example demonstrates how to manually access the USD Resolver to resolve a URI path.
While the `resolver.Resolve()` method is generic, this specific example is for an AYON context and resolves an AYON Entity URI.

For reference, the AYON Server supports two special versions: `HERO` and `latest`.
"""

from pxr import Ar

resolver = Ar.GetResolver()

project_name = "Experiments"
folder_path = "/things/deadline_submissions"
product = "pointcacheTestBgeo"
version = "latest" # "v008" # "HERO"
representation = "bgeo.sc"

unresolved_path = f"ayon+entity://{project_name}{folder_path}?product={product}&version={version}&representation={representation}"
resolved_path = resolver.Resolve(unresolved_path)
print(f"Resolved path: {resolved_path}")