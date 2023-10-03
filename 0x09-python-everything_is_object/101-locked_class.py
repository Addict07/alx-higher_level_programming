#!/usr/bin/python3
"""Defines a locked class."""


class LockedClass:
    """
    User cannot create new LockedClass attributes
    for anything called 'first_name'.
    """

    __slots__ = ["first_name"]
