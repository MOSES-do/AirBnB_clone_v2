#!/usr/bin/python3
""" Amenity Module for HBNB project """
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.base_model import BaseModel
from models.base_model import Base


class Amenity(BaseModel, Base):
    name = ""

    __tablename__ = "amenities"
    name = Column(String(128), nullable=False)
