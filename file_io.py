import json
from hospital import Hospital
from department import Department
from patient import Patient
from staff import Staff

def save_hospital_data(hospital, filename="hospital_data.json"):
    """Save all hospital data to a JSON file."""
    data = {
        "name": hospital.name,
        "location": hospital.location,
        "departments": []
    }
    
    for dept in hospital.departments:
        dept_data = {
            "name": dept.name,
            "patients": [],
            "staff": []
        }
        
        for patient in dept.patients:
            dept_data["patients"].append({
                "name": patient.name,
                "age": patient.age,
                "medical_record": patient.medical_record
            })
        
        for staff in dept.staff:
            dept_data["staff"].append({
                "name": staff.name,
                "age": staff.age,
                "position": staff.position
            })
        
        data["departments"].append(dept_data)
    
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)
    print(f"Data saved successfully to {filename}")


def load_hospital_data(filename="hospital_data.json"):
    """Load hospital data from a JSON file and return a Hospital object."""
    try:
        with open(filename, "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        print(f"File {filename} not found. Returning empty hospital.")
        return None
    

    
    hospital = Hospital(data["name"], data["location"])
    
    for dept_data in data["departments"]:
        dept = Department(dept_data["name"])
        
        for patient_data in dept_data["patients"]:
            patient = Patient(patient_data["name"], patient_data["age"], patient_data["medical_record"])
            dept.add_patient(patient)
        
        for staff_data in dept_data["staff"]:
            staff = Staff(staff_data["name"], staff_data["age"], staff_data["position"])
            dept.add_staff(staff)
        
        hospital.add_department(dept)
    
    print(f"Data loaded successfully from {filename}")
    return hospital


def search_patient_by_name(hospital, name):
    """Search for a patient by name across all departments."""
    results = []
    for dept in hospital.departments:
        for patient in dept.patients:
            if patient.name.lower() == name.lower():
                results.append({
                    "department": dept.name,
                    "patient": patient
                })
    return results


def search_staff_by_name(hospital, name):
    """Search for staff by name across all departments."""
    results = []
    for dept in hospital.departments:
        for staff in dept.staff:
            if staff.name.lower() == name.lower():
                results.append({
                    "department": dept.name,
                    "staff": staff
                })
    return results


def display_all_patients(hospital):
    """Display all patients in the hospital."""
    print("\n===== All Patients =====")
    for dept in hospital.departments:
        print(f"\nDepartment: {dept.name}")
        if not dept.patients:
            print("  No patients.")
        for patient in dept.patients:
            print(f"  - {patient.view_info()}, Record: {patient.medical_record}")


def display_all_staff(hospital):
    """Display all staff in the hospital."""
    print("\n===== All Staff =====")
    for dept in hospital.departments:
        print(f"\nDepartment: {dept.name}")
        if not dept.staff:
            print("  No staff.")
        for staff in dept.staff:
            print(f"  - {staff.view_info()}")