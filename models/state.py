#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy.orm import Relationship
from sqlalchemy import String, Integer, Column


class State(BaseModel):
    """ State class """
    __tablename__ = "states"

    name = ""

    cities = Relationship("City", passive_deletes=True, back_populates="state")
    name = Column(String(128), nullable=False)

    def cities(self):
        """getter attribute"""
        city_list = []
        for key, value in cities.items():
            state_id = value.get('state_id')
            if state_id == State.id:
                city_list = cities
