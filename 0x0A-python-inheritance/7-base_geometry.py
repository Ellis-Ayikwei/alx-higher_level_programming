#!/usr/bin/python3

"""Defines a base geometry class BaseGeometry."""


class BaseGeometry:
    """Represent base geometry."""

    def area(self):
        """Not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate a parameter as an inter and also
        check if its a positive number
        Args:
            name (str): the name of the parameter.
            value (int): The parameter to validate.
        Raises:
            TypeError: if the value in not an int.
            valueError: if the value is less than or equal to 0
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value >= 0:
            raise ValueError("{} must be greater than 0".format(name))
