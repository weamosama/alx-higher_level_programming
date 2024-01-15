#!/usr/bin/python3
""" Module defining the Square class. """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ The Square class, inheriting from Rectangle. """

    def __init__(self, size, x=0, y=0, id=None):
        """ Constructor for Square class.

        Args:
            size (int): The size of the square.
            x (int): The x-coordinate of the square.
            y (int): The y-coordinate of the square.
            id (int): The identifier for the instance.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ Getter for the size attribute. """
        return self.width

    @size.setter
    def size(self, value):
        """ Setter for the size attribute.

        Args:
            value (int): The value to set for size.
        """
        self.width = value
        self.height = value

    def __str__(self):
        """ String representation of the square.

        Returns:
            str: [Square] (<id>) <x>/<y> - <size>
        """
        return "[Square] ({}) {}/{} - {}".format(
         self.id, self.x, self.y, self.width
         )
