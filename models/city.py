#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, Integer, ForeignKey


class City(BaseModel, Base):
    """ The city class, contains state ID and name
    from state import State"""
    __tablename__ = 'cities'

    state_id = ""
    name = ""

    name = Column(String(128), nullable=False)
    """
    cascade - when a row in the referenced table i s deleted,
    the corresponding row in the current table is also deleted
    """
    state_id = Column(
        String(60), ForeignKey("states.id", ondelete="CASCADE"),
        nullable=False
    )
    places = relationship("Place", passive_deletes=True, backref="cities")
