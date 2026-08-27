from person import Person

class Patient(Person):
    """Class for hospital patients, inheriting from Person."""

    def __init__(self, name, age, medical_record):
        super().__init__(name, age)

        # Medical record validation
        if not isinstance(medical_record, str): #to check if the medical report is string
            raise TypeError("Medical record must be a string.")

        if not medical_record.strip(): #to check if the medical report is empty or has only spaces
            raise ValueError("Medical record cannot be empty.")

        self.medical_record = medical_record

    def view_record(self):
        """View patient record."""
        return f"Patient Record: {self.medical_record}"