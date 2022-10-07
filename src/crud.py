from sqlalchemy.orm import Session

from . import db_models as models, schemas


def get_results(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Result).offset(skip).limit(limit).all()


def create_result(db: Session, result: schemas.StoreResult):
    db_result = models.Result(image=result.image, coordinates=result.coordinates)
    db.add(db_result)
    db.commit()
    db.refresh(db_result)
    return db_result

