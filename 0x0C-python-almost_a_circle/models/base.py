#!/usr/bin/python3
"""Defines a model class named base"""


class Base:
    """Defines a base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Method that assign the public instance attribute id

           Args:
               id(int): integer value to manage id

           Return:
               Always nothing.

        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
    
    @staticmethod        
    def to_json_string(list_dictionaries):
        """ returns the JSON string representation of list_dictionaries"""
        """Method that returns the JSON
           string representation

        Args:
           list_dictionaries(dict): List of dictionaries

        Return:
           JSON string
        """
        if list_dictionaries is None or bool(list_dictionaries) is False:
            return "[]"
        else:
            json_rep = json.dumps(list_dictionaries)
            return json_rep
        
        
    @classmethod
    def save_to_file(cls, list_objs):
        """ Method that writes the JSON string representation
            of list_objs to a file

        Args:
            list_objs(list): List of objects

        Return:
           Nothing
        """
        filename = "{}.json".format(cls.__name__)
        list_dictionaries = []
        if list_objs is not None:
            for obj in list_objs:
                dictionary = obj.to_dictionary()
                list_dictionaries.append(dictionary)
            json_string = Base.to_json_string(list_dictionaries)
        with open(filename, 'w') as f:
            if list_objs is None:
                f.write("[]")
            else:
                f.write(json_string)

