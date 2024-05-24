#!/usr/bin/python3
""" Place Module for HBNB project """
from sqlalchemy import Column, String, Integer, ForeignKey, Float, Table
from sqlalchemy.orm import relationship
from models.base_model import BaseModel
from models.base_model import Base
from models.amenity import Amenity
import os


hbnb_storage = os.environ.get('HBNB_TYPE_STORAGE')
if hbnb_storage == 'db':
    place_amenity = Table('place_amenity', Base.metadata,
                          Column('place_id', String(60),
                                 ForeignKey('places.id', onupdate='CASCADE',
                                            ondelete='CASCADE'),
                                 primary_key=True),
                          Column('amenity_id', String(60),
                                 ForeignKey('amenities.id', onupdate='CASCADE',
                                            ondelete='CASCADE'),
                                 primary_key=True))


class Place(BaseModel, Base):
    """ A place to stay """
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

    __tablename__ = "places"

    city_id = Column(
        String(60), ForeignKey("cities.id", ondelete="CASCADE"),
        nullable=False
    )
    user_id = Column(
        String(60), ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False
    )
    reviews = relationship(
        "Review", passive_deletes=True,
        backref="places"
    )
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float)
    amenities = relationship(
        "Amenity", secondary='place_amenity',
        backref='places',
        viewonly=False
    )

    if hbnb_storage != 'db':
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

        @property
        def amenities(self):
            """getter attribute returns the list of Amenity instances"""
            from models.amenity import Amenity
            amenity_list = []
            all_amenities = storage.all(Amenity)
            for amenity in all_amenities.values():
                if amenity.place_id == self.id:
                    amenity_list.append(amenity)
            return amenity_list
