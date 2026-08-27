class Person:
    """Base class for all people in the hospital."""

    def __init__(self, name, age):
        # Name validation
        if not isinstance(name, str): #to check if the name is string
            raise TypeError("Name must be a string.")

        if not name.strip(): #to check if the name is has only spaces or is empty
            raise ValueError("Name cannot be empty.")

        # Age validation
        if not isinstance(age, int): #to check if the age is string or not
            raise TypeError("Age must be an integer.")

        if age <= 0:
            raise ValueError("Age must be greater than 0.")

        self.name = name
        self.age = age

    def view_info(self):
        """View basic information about the person."""
        return f"Name: {self.name}, Age: {self.age}"