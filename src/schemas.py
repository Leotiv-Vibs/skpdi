from pydantic import BaseModel


class StoreResult(BaseModel):
    image: bytes
    coordinates: dict

    class Config:
        orm_mode = True


class Result(BaseModel):
    coordinates: dict
    id: int

    class Config:
        orm_mode = True
