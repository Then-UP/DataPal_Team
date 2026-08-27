from patient import Patient
from staff import Staff

class Department:
    """Class representing a department in the hospital."""

    def __init__(self, name):
        # Department validation
        if not isinstance(name, str): #to check if the name is string
            raise TypeError("Department name must be a string.")

        if not name.strip(): #to check if the name is empty or has only spaces
            raise ValueError("Department name cannot be empty.")

        self.name = name
        self.patients = []
        self.staff = []

    def add_patient(self, patient):
        """Add a patient to the department."""
        if not isinstance(patient, Patient): #to check if the patient is an object from the class patient
            raise TypeError("Expected a Patient object.")

        self.patients.append(patient)
        print(f"Patient '{patient.name}' added to {self.name} department.")

    def add_staff(self, staff_member):
        """Add staff member to the department."""
        if not isinstance(staff_member, Staff): #to check if the staff member is an object from the class patient
            raise TypeError("Expected a Staff object.")

        self.staff.append(staff_member)
        print(f"Staff '{staff_member.name}' added to {self.name} department.")

    def search_patient(self, name):
        name = name.strip().lower()
        result = []
        for p in self.patients:
            if name in p.name.lower():
                result.append(p)
        return result

    def department_summary(self):
        lines = [f"---Department: {self.name} ---"]
        lines.append(f"  Staff ({len(self.staff)}):")
        if self.staff:
            for s in self.staff:
                lines.append(f"       -{s.view_info()}")
        else:
            lines.append("     (no staff assigned)")

        lines.append(f"   Patients  ({len(self.patients)}): ")
        if self.patients:
            for p in self.patients:
                lines.append(f"     - {p.view_info()}  | {p.view_record()}")
        else:
            lines.append("  (no patients registered)")

        return "\n".join(lines)