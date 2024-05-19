#!/usr/bin/python3
""" Place Module for HBNB project """
from sqlalchemy import Column, String, Integer, ForeignKey, Float
from sqlalchemy.orm import relationship
from models.base_model import BaseModel
from models.base_model import Base


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []

    city_id = Column(
        String(60), ForeignKey("cities.id", ondelete="CASCADE"),
        nullable=False
    )
    user_id = Column(
        String(60), ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False
    )
    reviews = relationship("Review", passive_deletes=True, backref="Place")
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, nullable=False)
    number_bathrooms = Column(Integer, nullable=False)
    max_guest = Column(Integer, nullable=False)
    price_by_night = Column(Integer, nullable=False)
    latitude = Column(Float)
    longitude = Column(Float)

    @property
    def reviews(self):
        """Getter attribute reviews that returns the list of Review
        instances with place_id equals to the current Place.id"""
        from models.__init__ import storage
        all_reviews = storage.all(Review)
        reviews = all_reviews.values()
        place_reviews = [
            review for review in reviews if review.place_id == self.id
        ]
        return place_reviews
