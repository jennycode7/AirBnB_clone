#!/usr/bin/python3
'''
A model
'''
from models.base_model import BaseModel


class Place(BaseModel):
    '''
    A class
    '''
    city_id = ''
    user_id = ''
    name = ''
    description = ''
    number_rooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0
    longitude = 0
    amenity_ids = ''
    number_bathrooms = 0