from person import Person

class Staff(Person):
    """Class for hospital staff, inheriting from Person."""

    def __init__(self, name, age, position):
        super().__init__(name, age)

        # Position validation
        if not isinstance(position, str): #to check if the position is string
            raise TypeError("Position must be a string.")

        if not position.strip(): #to check if the position is empty or has only spaces
            raise ValueError("Position cannot be empty.")

        self.position = position

    def view_info(self):
        """View staff information."""
        return (
            f"Staff Name: {self.name}, "
            f"Age: {self.age}, "
            f"Position: {self.position}"
        )