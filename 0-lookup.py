#!/usr/bin/python3
"""
Module for lookup function.
Contains a single function to return available attributes and methods of an object.
"""

def lookup(obj):
    """Returns the list of available attributes and methods of an object."""
    return dir(obj)
