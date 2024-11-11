#!/usr/bin/python3
"""
Module for MyList class that inherits from list.
Contains a method to print the list in sorted order.
"""


class MyList(list):
    """A subclass of list with a method to print the list sorted in ascending order."""

    def print_sorted(self):
        """
        Prints the list in ascending sorted order.
        The original list remains unmodified.
        """
        print(sorted(self))


# Example usage:
if __name__ == "__main__":
    my_list = MyList()
    my_list.append(3)
    my_list.append(1)
    my_list.append(2)
    my_list.print_sorted()  # Should print [1, 2, 3]
    print(my_list)  # Should print [3, 1, 2]
