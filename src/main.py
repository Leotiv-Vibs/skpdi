import io
import json
from typing import List

import torch
from fastapi import FastAPI, File, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from PIL import Image

from src import crud, db_models, schemas
from .database import SessionLocal, engine

db_models.Base.metadata.create_all(bind=engine)


# wget --load-cookies /tmp/cookies.txt "https://docs.google.com/uc?export=download&confirm=$(wget --quiet --save-cookies /tmp/cookies.txt --keep-session-cookies --no-check-certificate 'https://docs.google.com/uc?export=download&id=19xSpzu8QK1McwHQyUcMpfZxnQsQPRvPw' -O- | sed -rn 's/.*confirm=([0-9A-Za-z_]+).*/\1\n/p')&id=19xSpzu8QK1McwHQyUcMpfZxnQsQPRvPw" -O best.pt && rm -rf /tmp/cookies.txt


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_yolov5():
    model = torch.hub.load('/opt/yolov5', 'custom',
                           path='/opt/best.pt',
                           source='local')
    model.conf = 0.5
    return model


def get_image_from_bytes(binary_image, max_size=416):
    input_image = Image.open(io.BytesIO(binary_image)).convert("RGB")
    width, height = input_image.size
    resize_factor = min(max_size / width, max_size / height)
    resized_image = input_image.resize((
        int(input_image.width * resize_factor),
        int(input_image.height * resize_factor)
    ))
    return resized_image


model = get_yolov5()
app = FastAPI(
    title="Custom YOLOV5 Machine Learning API",
    description="""Obtain object value out of image
    and return image and json result""",
    version="0.0.1",
)
origins = [
    "http://localhost",
    "http://localhost:8000",
    "*"
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/results/", response_model=List[schemas.Result])
def read_results(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    results = crud.get_results(db, skip=skip, limit=limit)
    return results


@app.get('/notify/v1/health')
def get_health():
    return dict(msg='OK')


@app.post("/results/", response_model=schemas.Result)
async def create_result(
        file,
        db: Session = Depends(get_db)):
    data = json.load(file)
    image = data['image']
    id_object = data['id_object']
    class_object = data['class_object']
    timestamp = data['timestamp']
    latitude = data['latitude']
    latitude_direction = data['latitude_direction']
    longitude = data['longitude']
    longitude_direction = data['longitude_direction']
    gps_quality_indicator = data['gps_quality_indicator']
    number_satellites = data['number_satellites']
    horizontal_dilution_precision = data['horizontal_dilution_precision']
    antenna_alt_above_sea_level = data['antenna_alt_above_sea_level']
    units_altitude = data['units_altitude']
    geoidal_separation = data['geoidal_separation']
    units_geoidal_separation = data['units_geoidal_separation']
    age_differential_gps_data = data['age_differential_gps_data']
    differential_reference_station = data['differential_reference_station']
    detect_res = data['coordinates']
    result = schemas.StoreResult(coordinates=detect_res,
                                 image=image,
                                 id_object=id_object,
                                 class_object=class_object,
                                 timestamp=timestamp,
                                 latitude=latitude,
                                 latitude_direction=latitude_direction,
                                 longitude=longitude,
                                 longitude_direction=longitude_direction,
                                 gps_quality_indicator=gps_quality_indicator,
                                 number_satellites=number_satellites,
                                 horizontal_dilution_precision=horizontal_dilution_precision,
                                 antenna_alt_above_sea_level=antenna_alt_above_sea_level,
                                 units_altitude=units_altitude,
                                 geoidal_separation=geoidal_separation,
                                 units_geoidal_separation=units_geoidal_separation,
                                 age_differential_gps_data=age_differential_gps_data,
                                 differential_reference_station=differential_reference_station
                                 )
    created = crud.create_result(db, result)
    return created
