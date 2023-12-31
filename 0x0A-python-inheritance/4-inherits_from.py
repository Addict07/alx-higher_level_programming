#!/usr/bin/python3
"""Defines inherited class-checking function."""


def inherits_from(obj, a_class):
    """verifies if an object is an inherited instance of a class.

    Args:
        obj : The object to be checked.
        a_class (type): The class to match the type of obj to.
    Returns:
        For inherited instance of a_class - True.
        Otherwise - False.
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
