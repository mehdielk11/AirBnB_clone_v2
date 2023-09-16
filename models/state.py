#!/usr/bin/python3
'''
    Implementation of the State class
'''

from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import models
import os


class State(BaseModel, Base):
    '''
        Implementation for the State.
    '''
    __tablename__ = 'states'

    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        name = Column(String(128), nullable=False)

        cities = relationship("City", passive_deletes=True, backref="state")

    else:
        name = ""

        @property
        def cities(self):
            '''
                Returns all cities associated with current state instance
            '''
            cities = [v for k, v in models.storage.all().items()
                      if 'City' in k and v.state_id == self.id]
            return cities
