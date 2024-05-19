#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy.orm import relationship
from sqlalchemy import String, Integer, Column
from models.city import City
import models


class State(BaseModel, Base):
    """ State class """
    name = ""

    __tablename__ = "states"
    """
    passive_del=true means when a child entity in a relationship btw
    a parent and child e.g State and city, is deleted the parent entity
    remains but if the parent entity is deleted all the children entity
    associated with the parent by reaso of a foreign key are deleted
    This ensures referential integrity
    """
    """
    Relationship(City) - defines relationship btw State and city entity
    such that State will have a collection of cities.
    A one to many relationship
    """
    cities = relationship("City", passive_deletes=True, backref="state")
    name = Column(String(128), nullable=False)

    @property
    def cities(self):
        """getter attribute"""
        city_list = []
        all_cities = models.storage.all(City)
        for city in all_cities.values():
            if city.state_id == self.id:
                city_list.append(city)
        return city_list
