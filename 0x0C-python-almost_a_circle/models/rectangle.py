#!/usr/bin/python3
"""
Rectangle module
"""
from models.base import Base


class Rectangle(Base):
    """
    Rectangle class, inherits from Base
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes a new instance of Rectangle
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def area(self):
        """
        Calculates the area of the rectangle
        """
        return self.width * self.height

    def display(self):
        """
        Displays the rectangle using '#' characters
        """
        for _ in range(self.y):
            print()
        for _ in range(self.height):
            print(' ' * self.x + '#' * self.width)

    def __str__(self):
        """
        String representation of the rectangle
        """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """
        Updates the attributes of the rectangle
        """
        if args:
            attrs = ['id', 'width', 'height', 'x', 'y']
            for i, value in enumerate(args):
                setattr(self, attrs[i], value)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """
        Returns the dictionary representation of the rectangle
        """
        return {'id': self.id, 'width': self.width, 'height': self.height,
                'x': self.x, 'y': self.y}
