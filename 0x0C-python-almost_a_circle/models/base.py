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
         if id != None:
             self.id = id
         else:
             Base.__nb_objects += 1
             self.id = Base.__nb_objects
