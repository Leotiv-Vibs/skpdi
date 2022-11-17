from datetime import datetime

from sqlalchemy import Column, JSON, Integer, String, DateTime, LargeBinary
from sqlalchemy.dialects.postgresql import JSONB

from .database import Base
# CREATE TABLE public.t_skpdi( id integer NOT NULL, image_base text COLLATE pg_catalog."default", labels text COLLATE pg_catalog."default", id_object integer, class_object integer, timestamp text, latitude text, latitude_direction text, longitude text, longitude_direction text, gps_quality_indicator text, number_satellites text, horizontal_dilution_precision text, antenna_alt_above_sea_level text, units_altitude text, geoidal_separation text, units_geoidal_separation text, age_differential_gps_data text, differential_reference_station text)
# CREATE SEQUENCE public.t_skpdi_id_seq START WITH 1 INCREMENT BY 1 NO MINVALUE NO MAXVALUE CACHE 1
# ALTER SEQUENCE public.t_skpdi_id_seq OWNED BY public.t_skpdi.id
# ALTER TABLE ONLY public.t_skpdi ALTER COLUMN id SET DEFAULT nextval('public.t_skpdi_id_seq'::regclass)
# INSERT INTO t_skpdi(image_base, labels,id_object,class_object,timestamp,latitude,latitude_direction,longitude,longitude_direction,gps_quality_indicator,number_satellites,horizontal_dilution_precision,antenna_alt_above_sea_level,units_altitude,geoidal_separation,units_geoidal_separation,age_differential_gps_data,differential_reference_station) VALUES ('asd','asd',1,1,'asd','asd','asd','asd','asd','asd','asd','asd','asd','asd','asd','asd','asd','asd')


class Result(Base):
    __tablename__ = "results"

    id = Column(Integer, primary_key=True, index=True)
    created_at = Column(DateTime, default=datetime.now)
    image = Column(LargeBinary, default=False)
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
