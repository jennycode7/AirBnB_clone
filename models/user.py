#!/usr/bin/python3
'''
A model
'''
from models.base_model import BaseModel

class User(BaseModel):
    '''
    A class
    '''
    def __init__(self, *args, **kwargs):
        '''
        Initializer
        '''
        super().__init__(*args, **kwargs)
        self.email = ""
        self.password = ""
        self.first_name = ""
        self.last_name = ""
