#!/usr/bin/python3
"""
Module for MyList class that inherits from list.
Contains a method to print the list in sorted order.
"""


class MyList(list):
    """A subclass of list with a method to print the list sorted in ascending order."""

    def print_sorted(self):
        """Prints the list in ascending sorted order."""
        print(sorted(self))
