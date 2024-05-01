#!usr/bin/python3
'''
A model
'''
import uuid
import datetime


class BaseModel:
    '''
    A class
    '''
    def __init__(self):
        '''
        To initialize self
        '''
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = self.created_at

    def __str__(self):
        '''
        mainipulates str
        '''
        return "[{}] ({}) {}".format(BaseModel.__name__,
                                     self.id, self.__dict__)

    def save(self):
        '''
        updates self
        '''
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        '''
        converts to dictionary
        '''
        to_obj = self.__dict__.copy()
        to_obj['name'] = self.__class__.__name__
        to_obj['created_at'] = self.created_at.isoformat()
        to_obj['updated_at'] = self.updated_at.isoformat()
        return to_obj
