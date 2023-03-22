#!/usr/bin/python3
""" Place Module for HBNB project """
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship

import models
from models.base_model import BaseModel, Base
from models.review import Review

place_amenity = Table(
    "place_amenity",
    Base.metadata,
    Column(
        "place_id",
        String(60),
        ForeignKey("places.id"),
        primary_key=True,
        nullable=False,
    ),
    Column(
        "amenity_id",
        String(60),
        ForeignKey("amenities.id"),
        primary_key=True,
        nullable=False,
    ),
)


class Place(BaseModel, Base):
    """A place to stay"""

    __tablename__ = "places"

    description = Column(String(1024))
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float)
    longitude = Column(Float)
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    reviews = relationship("Review", cascade="all, delete", backref="place")
    amenities = relationship("Amenity", secondary=place_amenity, viewonly=False)

    @property
    def reviews(self):
        result = []
        reviews_ = models.storage.all(Review)
        for key, value in reviews_.items():
            if value.place_id == self.id:
                result.append(value)
        return result
