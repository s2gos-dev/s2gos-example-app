from pathlib import Path
from typing import Optional

import s2gos_simulator.main
from s2gos_common.models import Link
from s2gos_scene_description.scene import Scene

from s2gos_server.provider import get_service
from s2gos_simulator.core import ObservationSpecification, OutputSpecification

service = get_service()


@service.process(
    id="simulate_observation",
    title="Simulate S2GOS observations.",
    description=(
        "Simulates observation from a scene that follows the scene description standard. "
        "Saves it as netcdf in a temporary location. "
        "Requires installed dask, xarray, and zarr packages."
    ),
    inline_inputs=["scene", "observation_spec", "output_spec", "output_path"],
)
def simulate_observation(
    scene: Scene,
    observation_spec: ObservationSpecification,
    output_spec: OutputSpecification,
    output_path: Optional[str] = None,
) -> Link:
    """Generate synthetic scene using external library."""

    # Call external library - stateless function
    result = s2gos_simulator.main.simulate_observation(
        scene,
        observation_spec,
        output_spec,
    )

    if not output_path:
        output_path = "file://s2gos_example_app/result/output.zarr"

    result.to_zarr(output_path, mode="w")
    if "://" in output_path:
        href = output_path
    else:
        href = Path(output_path).resolve().as_uri()

    return Link(href=href, type="application/zarr")
