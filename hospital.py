from department import Department

class Hospital:
    """Class for managing hospital operations."""

    def __init__(self, name, location):
        # Hospital name validation
        if not isinstance(name, str): #to check if the name is string
            raise TypeError("Hospital name must be a string.")

        if not name.strip(): #to check if the position is empty or has only spaces
            raise ValueError("Hospital name cannot be empty.")

        # Location validation
        if not isinstance(location, str): #to check if the location is string
            raise TypeError("Location must be a string.")

        if not location.strip(): #to check if the location is empty or has only spaces
            raise ValueError("Location cannot be empty.")

        self.name = name
        self.location = location
        self.departments = []

    def add_department(self, department):
        """Add a department to the hospital."""
        if not isinstance(department, Department): #to check if the location is an object from the class department
            raise TypeError("Expected a Department object.")

        self.departments.append(department)
        print(f"Department '{department.name}' added to {self.name}.")

    def search_patient_by_name(self, name):
        results = []
        for dept in self.departments:
            matches = dept.search_patient(name)
            for patient in matches:
                results.append((patient, dept.name))
        return results

    def total_patients(self):
        return sum(len(dept.patients) for dept in self.departments)
        
    def total_staff(self):
        return sum(len(dept.staff) for dept in self.departments)

    def generate_report(self):
        lines = []
        lines.append("=" * 50)
        lines.append(f"HOSPITAL REPORT: {self.name}")
        lines.append(f"Location: {self.location}")
        lines.append("=" * 50)
        lines.append(f"Total Departments : {len(self.departments)}")
        lines.append(f"Total Staff      :{self.total_staff()}")
        lines.append(f"Total Patient     : {self.total_patients()}")

        if not self.departments:
            lines.append("(No departments have been added yet.)")
        else:
            for dept in self.departments:
                lines.append(dept.department_summary())
                lines.append("")

        report ="\n".join(lines)
        print(report)
        return report