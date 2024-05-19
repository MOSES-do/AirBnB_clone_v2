#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy.orm import relationship
from sqlalchemy import String, Integer, Column


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

    def cities(self):
        """getter attribute"""
        city_list = []
        for key, value in cities.items():
            state_id = value.get('state_id')
            if state_id == State.id:
                city_list = cities
