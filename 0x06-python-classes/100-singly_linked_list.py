#!/usr/bin/python3

class Node:
    """
    Class documentation goes here
    """
    def __init__(self, data, next_node=None):
        """
        Method documentation goes here
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        Getter method for data attribute
        """
        return self.__data

    @data.setter
    def data(self, value):
        """
        Setter method for data attribute
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")

        self.__data = value

    @property
    def next_node(self):
        """
        Getter method for next_node attribute
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        Setter method for next_node attribute
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")

        self.__next_node = value


class SinglyLinkedList:
    """
    Class documentation goes here
    """
    def __init__(self):
        """
        Method documentation goes here
        """
        self.head = None

    def sorted_insert(self, value):
        """
        Method documentation goes here
        """
        new_node = Node(value)

        if self.head is None or value < self.head.data:
            new_node.next_node = self.head
            self.head = new_node
            return

        current = self.head
        while current.next_node is not None and current.next_node.data < value:
            current = current.next_node

        new_node.next_node = current.next_node
        current.next_node = new_node

    def __str__(self):
        """
        Method documentation goes here
        """
        result = []
        current = self.head
        while current is not None:
            result.append(str(current.data))
            current = current.next_node
        return "\n".join(result)
