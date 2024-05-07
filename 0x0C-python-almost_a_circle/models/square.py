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
