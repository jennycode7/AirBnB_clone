#!/usr/bin/python3
'''
A model
'''
from models.base_model import BaseModel


class Review(BaseModel):
    '''
    A class
    '''
    place_id = ''
    user_id = ''
    text = ''
