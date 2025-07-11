from pydantic import BaseModel


class Scene(BaseModel):
    DEM_mesh_path: str
    landcover_texture_path: str
