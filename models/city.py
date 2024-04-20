#!/usr/bin/python3
""" City Module for HBNB project """
from sqlalchemy.orm import Relationship
from models.base_model import BaseModel
from sqlalchemy import Column, String, Integer, ForeignKey


class City(BaseModel):
    """ The city class, contains state ID and name
    from state import State"""
    __tablename__ = 'cities'

    state_id = ""
    name = ""

    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey("states.id", ondelete="CASCADE"))
