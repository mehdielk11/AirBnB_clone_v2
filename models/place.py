#!/usr/bin/python3
'''
    Define the class Place.
'''
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.schema import Table
import models
import os


if os.getenv('HBNB_TYPE_STORAGE') == 'db':
    association_table = Table('place_amenity', Base.metadata,
        Column('place_id', String(60), ForeignKey('places.id'),
               nullable=False, primary_key=True),
        Column('amenity_id', String(60), ForeignKey('amenities.id'),
               nullable=False, primary_key=True))


class Place(BaseModel, Base):
    '''
        Define the class Place that inherits from BaseModel.
    '''
    __tablename__ = "places"

    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        city_id = Column(String(60), ForeignKey(
            'cities.id', ondelete='CASCADE'), nullable=False)
        user_id = Column(String(60), ForeignKey(
            'users.id', ondelete='CASCADE'), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024))
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float)
        longitude = Column(Float)

        reviews = relationship("Review", passive_deletes=True, backref="place")
        amenities = relationship(
            "Amenity", secondary=association_table, viewonly=False)

    else:
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

        @property
        def reviews(self):
            """
                Property reviews: reviews associated with place.id
            """
            reviews = models.storage.all(models.Review)
            my_reviews = []
            for review in reviews:
                if review.place_id == self.id:
                    my_reviews.append(review)
            return my_reviews

        @property
        def amenities(self):
            """
                Property amenities: amenities associated with place.id

                Setter validates obj is Amenity

                Parameter:
                    obj: object to append obj.id to amenity_ids
            """

            return Place.amenity_ids

        @amenities.setter
        def amenities(self, obj=None):
            if type(obj) is Amenity:
                Place.amenity_ids.append(obj.id)
