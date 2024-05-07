#!/usr/bin/python3
"""Define a square that inherits from the rectangle class
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Defines a Square Class"""

    def __init__(self, size, x=0, y=0, id=None):
        """Method that initialized the square

        Args:
           size: side's size of the square
           x: Position on x axis.
           y: Position on y axis.

        Return:
           Always nothing.

        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Method that returns a string"""
        return ("[Square] ({}) {}/{} - {}"
                .format(self.id, self.x, self.y,
                        self.width))

    # Getter and setter of width
    @property
    def width(self):
        """Getter for the size of width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for the size of width

        Args:
           value: Size to assign to the width

        Return:
           Always Nothing

        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    # Getter and setter of height
    @property
    def height(self):
        """Getter the size of height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Setter the size of height

        Args:
           value: Size to assign to the height

        Return:
           Always Nothing

        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value
