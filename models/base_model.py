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
    def __init__(self, *args, **kwargs):
        '''
        Initializes self
        '''
        if kwargs:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.datetime.strptime(value,
                                                       "%Y-%m-%dT%H:%M:%S.%f")
                setattr(self, key, value)
        else:
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
        to_obj['__class__'] = type(self).__name__
        to_obj['created_at'] = self.created_at.isoformat()
        to_obj['updated_at'] = self.updated_at.isoformat()
        return to_obj