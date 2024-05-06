#!/usr/bin/python3
"""inherits from Base"""
from models.base import Base


class Rectangle(Base):
    """Defines a rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Method that init values for a rectangle object

        Args:
           width:size of the width
           height: size of the height
           x: Variable x
           y:  Variable y

        Return:
           Always nothing

        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

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

    # Getter and setter for x variable
    @property
    def x(self):
        """Getter of x variable
        """
        return self.__x

    @x.setter
    def x(self, value):
        """Setter of x variable

        Args:
           value: value to assign to x variable

        Return:
           Always Nothing

        """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    # Getter and setter for y variable
    @property
    def y(self):
        """Getter of y variable
        """
        return self.__y

    @y.setter
    def y(self, value):
        """Setter of y variable

        Args:
           value: value to assign to y variable

        Return:
           Always Nothing

        """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value
