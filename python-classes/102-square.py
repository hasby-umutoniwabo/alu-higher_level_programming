#!/usr/bin/python3
"""
Module to define a Square class that represents a square with a given size.
"""


class Square:
    """Class to define a square with a specific size."""

    def __init__(self, size=0):
        """
        Initialize a new Square instance.

        Args:
            size (int or float): The size of the square. Default is 0.
        """
        self.size = size

    @property
    def size(self):
        """Retrieve the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square.

        Args:
            value (int or float): The new size of the square.

        Raises:
            TypeError: If size is not a number (int or float).
            ValueError: If size is less than 0.
        """
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current square area."""
        return self.size ** 2

    def __eq__(self, other):
        """Check if two squares are equal based on area."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Check if two squares are not equal based on area."""
        return self.area() != other.area()

    def __lt__(self, other):
        """Check if this square is less than another based on area."""
        return self.area() < other.area()

    def __le__(self, other):
        """Check if this square is less than or equal to another based on area."""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Check if this square is greater than another based on area."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Check if this square is greater than or equal to another based on area."""
        return self.area() >= other.area()


# Example usage and tests
if __name__ == "__main__":
    s_5 = Square(5)
    s_6 = Square(6)

    if s_5 < s_6:
        print("Square 5 < Square 6")
    if s_5 <= s_6:
        print("Square 5 <= Square 6")
    if s_5 == s_6:
        print("Square 5 == Square 6")
    if s_5 != s_6:
        print("Square 5 != Square 6")
    if s_5 > s_6:
        print("Square 5 > Square 6")
    if s_5 >= s_6:
        print("Square 5 >= Square 6")
