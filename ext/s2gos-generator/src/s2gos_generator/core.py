from pydantic import BaseModel


class SceneSpecification(BaseModel):
    DEM: str
    landcover: str
