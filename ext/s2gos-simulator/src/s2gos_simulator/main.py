import xarray as xr
from s2gos_scene_description.scene import Scene

from .core import ObservationSpecification, OutputSpecification


def simulate_observation(
    scene: Scene,
    observation_spec: ObservationSpecification,
    output_spec: OutputSpecification,
):
    return xr.Dataset()
