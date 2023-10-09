#!/usr/bin/python3
"""Defines a function that checks class."""


def is_same_class(obj, a_class):
    """This verifies if an object is exactly an instance of a given class.

    Args:
        obj : Object to be checked.
        a_class (type): The class to match the type of obj to.
    Returns:
        For object that is instance of a_class - True.
        Otherwise - False.
    """
    if type(obj) == a_class:
        return True
    return False
