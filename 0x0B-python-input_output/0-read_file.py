#!/usr/bin/python3
"""Defines the reading file function."""


def read_file(filename=""):
    """Print the content text file to stdout."""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
