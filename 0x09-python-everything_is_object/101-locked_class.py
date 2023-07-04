#!/usr/bin/python3
class LockedClass:
    """
    A class that prevents dynamically creating new instance attributes,
    except for 'first_name'.
    """

    def __setattr__(self, name, value):
        """
        Override the __setattr__ method to prevent creating new instance attributes,
        unless the attribute is 'first_name'.

        Args:
            name (str): Name of the attribute being set.
            value (Any): Value to be assigned to the attribute.

        Raises:
            AttributeError: If trying to create a new attribute other than 'first_name'.
        """
        if hasattr(self, name) or name == "first_name":
            super().__setattr__(name, value)
        else:
            raise AttributeError("'LockedClass' object has no attribute '{}'".format(name))
