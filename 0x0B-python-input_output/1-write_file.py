#!/usr/bin/python3
"""
Defines a file-writing function.
"""

def write_file(filename="", text=""):
    """
    Writes the given text to a file.

    Args:
        filename (str): The name of the file to be written.
        text (str): The text to be written to the file.

    Returns:
        int: The number of characters written to the file.

    Raises:
        FileNotFoundError: If the specified file path is invalid.
        PermissionError: If there are insufficient permissions to write to the file.
    """

    try:
        with open(filename, "w", encoding="utf-8") as t:
            return t.write(text)

    except FileNotFoundError:
        print(f"File '{filename}' not found.")
    except PermissionError:
        print(f"You don't have permission to write to file '{filename}'.")
