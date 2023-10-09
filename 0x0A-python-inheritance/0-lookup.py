#!/usr/bin/python3
"""This defines object attribute lookup function."""


def lookup(obj):
    """Will return list of an object's available attributes."""
    return (dir(obj))
