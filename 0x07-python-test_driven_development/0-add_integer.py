#!/usr/bin/python3
def add_integer(a, b=98):
    """
    Adds two integers together and returns the result.

    Parameters:
        a (int or float): The first number to be added.
        b (int or float): The second number to be added. Default value is 98.

    Returns:
        int: The sum of `a` and `b`.

    Raises:
        TypeError: If either `a` or `b` is not an integer or float.

    Examples:
        >>> add_integer(2, 3)
        5
        >>> add_integer(2.5, 3.8)
        6
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
