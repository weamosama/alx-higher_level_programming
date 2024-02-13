#!/usr/bin/python3
""" Module defining the Rectangle class. """
from models.base import Base


class Rectangle(Base):
    """ The Rectangle class, inheriting from Base. """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Constructor for Rectangle class.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int): The x-coordinate of the rectangle.
            y (int): The y-coordinate of the rectangle.
            id (int): The identifier for the instance.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ Getter for the width attribute. """
        return self.__width

    @width.setter
    def width(self, value):
        """ Setter for the width attribute.

        Args:
            value (int): The value to set for width.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        """ Getter for the height attribute. """
        return self.__height

    @height.setter
    def height(self, value):
        """ Setter for the height attribute.

        Args:
            value (int): The value to set for height.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        """ Getter for the x attribute. """
        return self.__x

    @x.setter
    def x(self, value):
        """ Setter for the x attribute.

        Args:
            value (int): The value to set for x.
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        """ Getter for the y attribute. """
        return self.__y

    @y.setter
    def y(self, value):
        """ Setter for the y attribute.

        Args:
            value (int): The value to set for y.
        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        """ Calculate the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self.__width * self.__height

    def display(self):
        """ Display the rectangle with #, considering x and y. """
        for _ in range(self.__y):
            print()
        for _ in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def __str__(self):
        """ String representation of the rectangle.

        Returns:
            str: [Rectangle] (<id>) <x>/<y> - <width>/<height>
        """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
         self.id, self.__x, self.__y, self.__width, self.__height
         )

    def update(self, *args, **kwargs):
        """ Update the attributes of the rectangle.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        """
        if args:
            attr_names = ["id", "width", "height", "x", "y"]
            for i, arg in enumerate(args):
                setattr(self, attr_names[i], arg)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """ Return the dictionary representation of a Rectangle.

        Returns:
            dict: The dictionary representation of the Rectangle.
        """
        return {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
        }
