from pathlib import Path
from typing import Optional

import s2gos_generator.main
from s2gos_common.models import Link
from s2gos_generator.core import SceneSpecification
from s2gos_scene_description.json_exporter import to_json
from s2gos_server.provider import get_service

service = get_service()


@service.process(
    id="generate_scene",
    title="Generate S2GOS scene given scene specification, returns a scene description.",
    description=(
        "Generate a synthetic scene given a . "
        "Saves it as netcdf in a temporary location. "
        "Requires installed dask, xarray, and zarr packages."
    ),
    inline_inputs=["scene_spec"],
)
def generate_scene(
    scene_spec: SceneSpecification,  # should follow the SceneSpecifcation...
    output_path: Optional[str] = None,
) -> Link:
    """Generate synthetic scene using external library."""

    print(scene_spec)
    print(type(scene_spec))
    # Call external library - stateless function
    scene = s2gos_generator.main.generate_scene(
        SceneSpecification(**scene_spec),
    )

    if not output_path:
        output_path = "file://s2gos_example_app/scene/scene.json"

    try:
        to_json(output_path, scene)
    except (OSError, IOError, PermissionError, FileNotFoundError) as e:
        print(f"Could not create JSON file: {e}")

    if "://" in output_path:
        href = output_path
    else:
        href = Path(output_path).resolve().as_uri()

    return Link(href=href, type="application/json")
