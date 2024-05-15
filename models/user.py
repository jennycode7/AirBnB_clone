#!/usr/bin/python3
'''
A model
'''
from models.base_model import BaseModel

class User(BaseModel):
    '''
    A class
    '''
    email = ''
    password = ''
    first_name = ''
    last_name = ''
