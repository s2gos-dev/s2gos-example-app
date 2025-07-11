from pydantic import BaseModel


class ObservationSpecification(BaseModel):
    viewing_zenith_angle: float
    viewing_azimuth_angle: float


class OutputSpecification(BaseModel):
    format: str  # would be an enum
