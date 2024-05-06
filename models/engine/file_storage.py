import json
from os import path

class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        key = "{}.{}".format(type(obj).__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        serialized_objects = {}
        for key, value in self.__objects.items():
            serialized_objects[key] = value.to_dict()

        with open(self.__file_path, 'w') as file:
            json.dump(serialized_objects, file)

    def reload(self):
        if path.exists(self.__file_path):
            from models.base_model import BaseModel
            with open(self.__file_path, 'r') as file:
                data = json.load(file)
                for key, value in data.items():
                    self.__objects[key] = eval(value['__class__'])(**value)
