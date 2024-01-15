#!/usr/bin/python3
""" Module defining the Base class. """


class Base:
    """ The Base class for managing id attribute. """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Constructor for Base class.

        Args:
            id (int): The identifier for the instance.
        """
        if id is not None:
            self.id = id
        else:
            type(self).__nb_objects += 1
            self.id = type(self).__nb_objects
