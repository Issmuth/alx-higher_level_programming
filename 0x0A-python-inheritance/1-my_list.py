#!/usr/bin/python3
"""Sub-class of the list class."""


class MyList(list):
    """Mylist object of the super class list."""

    def __init__(self):
        """Initializes the list object"""
        super().__init__()

    def print_sorted(self):
        """Prints the sorted form of the list."""
        print(sorted(self))
