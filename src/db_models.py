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
