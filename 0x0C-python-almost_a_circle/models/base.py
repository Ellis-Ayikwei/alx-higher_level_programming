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

