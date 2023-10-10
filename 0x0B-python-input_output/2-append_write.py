#!/usr/bin/python3
"""Defines an appending file function."""


def append_write(filename="", text=""):
    """Appends a string to text file.

    Args:
        filename (str): Name of the file to append to.
        text (str): String to append to the file.
    Returns:
        The number of characters appended.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
