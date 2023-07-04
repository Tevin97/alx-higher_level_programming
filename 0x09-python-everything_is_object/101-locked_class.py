#!/usr/bin/python3
class LockedClass:
    """
    A class that prevents the user from dynamically creating new instance attributes, except if the 
    new instance attribute is called first_name.
    """

    __slots__ = ("first_name",)

    def __setattr__(self, name, value):
        """
        Override the default setattr behavior to prevent dynamically creating new instance attributes,
        except if the attribute is called first_name.

        Args:
            name (str): The name of the attribute being set.
            value (Any): The value to be assigned to the attribute.

        Raises:
            AttributeError: If the attribute being set is not first_name and it doesn't already exist.
        """
        if not hasattr(self, name) and name != "first_name":
            raise AttributeError("Cannot create new instance attributes")
        super().__setattr__(name, value)
