from pydantic import BaseModel


class StoreResult(BaseModel):
    image: bytes
    coordinates: dict

    id_object: int
    class_object: int

    timestamp: str
    latitude: str
    latitude_direction: str
    longitude: str
    longitude_direction: str
    gps_quality_indicator: str
    number_satellites: str
    horizontal_dilution_precision: str
    antenna_alt_above_sea_level: str
    units_altitude: str
    geoidal_separation: str
    units_geoidal_separation: str
    age_differential_gps_data: str
    differential_reference_station: str

    class Config:
        orm_mode = True


class Result(BaseModel):
    coordinates: dict
    id: int

    id_object: int
    class_object: int

    timestamp: str
    latitude: str
    latitude_direction: str
    longitude: str
    longitude_direction: str
    gps_quality_indicator: str
    number_satellites: str
    horizontal_dilution_precision: str
    antenna_alt_above_sea_level: str
    units_altitude: str
    geoidal_separation: str
    units_geoidal_separation: str
    age_differential_gps_data: str
    differential_reference_station: str

    class Config:
        orm_mode = True
