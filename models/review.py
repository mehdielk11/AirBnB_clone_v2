#!/usr/bin/python3
'''
    Implementation of the Review class
'''
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
import os


class Review(BaseModel, Base):
    '''
        Implementation for the Review.
    '''
    __tablename__ = "reviews"

    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        text = Column(String(1024), nullable=False)
        place_id = Column(String(60), ForeignKey(
            'places.id', ondelete='CASCADE'), nullable=False)
        user_id = Column(String(60), ForeignKey(
            'users.id', ondelete='CASCADE'), nullable=False)

    else:
        text = ""
        place_id = ""
        user_id = ""
