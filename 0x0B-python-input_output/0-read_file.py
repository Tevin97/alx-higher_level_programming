#!/usr/bin/python3
"""Defines a text file-reading function."""


def read_file(filename=""):
    """
    Reads the contents of a file and prints it to the console.

    Args:
        filename (str): The name of the file to be read.

    Returns:
        None

    Raises:
        FileNotFoundError: If the specified file does not exist.
    """
    with open(filename, encoding="utf-8") as t:
        print(t.read(), end="")
