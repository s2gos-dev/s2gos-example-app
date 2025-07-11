from s2gos_scene_description.scene import Scene

from .core import SceneSpecification


def generate_scene(scene_spec: SceneSpecification) -> Scene:
    return Scene(
        DEM_mesh_path=scene_spec.DEM, landcover_texture_path=scene_spec.landcover
    )
