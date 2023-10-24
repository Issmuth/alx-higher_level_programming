#!/usr/bin/python3
# 101-singly_linked_lists.py by Ismael
"""Node object definition."""


class Node:
    """A node of a singly linked list."""

    def __init__(self, data, next_node=None):
        """Initialize first instance of node."""
        if not isinstance(data, int):
            raise TypeError("data must be an integer")
        if next_node is not None and not isinstance(next_node, Node):
            raise TypeError("next_node must be a Node object")
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Retrieve data."""
        return self.__data

    @data.setter
    def data(self, value):
        """Set data value.

        Args:
            value: value to be set
        Raises:
            TypeError: data must be an integer
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Retrives next node."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Set next node value."""
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """A singly linked list object."""

    def __init__(self):
        """Initialize a singly linked list."""
        self.head = None

    def __str__(self):
        """Make list printable."""
        lists = ""
        iterator = self.head
        while iterator is not None:
            lists += str(iterator.data) + "\n"
            iterator = iterator.next_node
        return lists[:-1]

    def sorted_insert(self, value):
        """Insert a new Node in increasing order.

        Args:
            value: value to be inserted
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        new_node = Node(value, None)
        if self.head is None:
            self.head = new_node
            return

        if self.head.data >= value:
            new_node.next_node = self.head
            self.head = new_node
            return

        iterate = self.head
        while iterate.next_node is not None and value > iterate.next_node.data:
            iterate = iterate.next_node

        new_node.next_node = iterate.next_node
        iterate.next_node = new_node
