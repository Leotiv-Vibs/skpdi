from sqlalchemy.orm import Session

from . import db_models as models, schemas


def get_results(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Result).offset(skip).limit(limit).all()


def create_result(db: Session, result: schemas.StoreResult):
    db_result = models.Result(image=result.image,
                              coordinates=result.coordinates,
                              id_object=result.id_object,
                              clss_object=result.class_object,
                              timestamp=result.timestamp,
                              latitude=result.latitude,
                              latitude_direction=result.latitude_direction,
                              longitude=result.longitude,
                              longitude_direction=result.longitude_direction,
                              gps_quality_indicator=result.gps_quality_indicator,
                              number_satellites=result.number_satellites,
                              horizontal_dilution_precision=result.horizontal_dilution_precision,
                              antenna_alt_above_sea_level=result.antenna_alt_above_sea_level,
                              units_altitude=result.units_altitude,
                              geoidal_separation=result.geoidal_separation,
                              units_geoidal_separation=result.units_geoidal_separation,
                              age_differential_gps_data=result.age_differential_gps_data,
                              differential_reference_station=result.differential_reference_station,
                              )
    db.add(db_result)
    db.commit()
    db.refresh(db_result)
    return db_result
