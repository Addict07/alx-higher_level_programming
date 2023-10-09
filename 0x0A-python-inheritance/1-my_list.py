#!/usr/bin/python3
"""This defines inherited list class MyList."""


class MyList(list):
    """Sorted printing for the built-in list class."""

    def print_sorted(self):
        """Will prinst a list in sorted ascending order."""
        print(sorted(self))
