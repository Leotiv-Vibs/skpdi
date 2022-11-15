from datetime import datetime

from sqlalchemy import Column, JSON, Integer, String, DateTime, LargeBinary
from sqlalchemy.dialects.postgresql import JSONB

from .database import Base


class Result(Base):
    __tablename__ = "results"

    id = Column(Integer, primary_key=True, index=True)
    created_at = Column(DateTime, default=datetime.now)
    image = Column(LargeBinary)
    coordinates = Column(JSONB)

    id_object = Column(Integer)
    class_object = Column(Integer)

    timestamp = Column(String)
    latitude = Column(String)
    latitude_direction = Column(String)
    longitude = Column(String)
    longitude_direction = Column(String)
    gps_quality_indicator = Column(String)
    number_satellites = Column(String)
    horizontal_dilution_precision = Column(String)
    antenna_alt_above_sea_level = Column(String)
    units_altitude = Column(String)
    geoidal_separation = Column(String)
    units_geoidal_separation = Column(String)
    age_differential_gps_data = Column(String)
    differential_reference_station = Column(String)
