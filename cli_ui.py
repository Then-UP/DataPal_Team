import os

# General helper functions

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def print_header(title):
    width = 50
    print("\n" + "=" * width)
    print(title.center(width))
    print("=" * width)

def print_divider():
    print("-" * 50)

def print_message(message, kind="info"):
    icons = {"success": "[OK]", "error": "[ERROR]", "info": "[INFO]"}
    tag = icons.get(kind, "[INFO]")
    print(f"{tag} {message}")

# Welcome screen

def print_welcome_screen():
    clear_screen()
    print("=" * 50)
    print("     WELCOME TO THE HOSPITAL MANAGEMENT SYSTEM".center(50))
    print("=" * 50)

def print_hospital_banner(hospital_name, hospital_location):
    print(f"\nHospital: {hospital_name}   |   Location: {hospital_location}")

# Main menu

MAIN_MENU_OPTIONS = {
    "1": "Add Department",
    "2": "Register Patient",
    "3": "Register Staff",
    "4": "Search Patient by Name",
    "5": "View Full Hospital Report",
    "6": "Save Data to File",
    "0": "Exit",
}

def show_main_menu():
    print_header("MAIN MENU")
    for key, label in MAIN_MENU_OPTIONS.items():
        print(f"  {key}. {label}")
    print_divider()
    choice = input("Enter your choice: ").strip()
    return choice


# --- دالة الحماية الجديدة (Input Validation) ---
def get_valid_age(prompt):
    while True:
        age_input = input(prompt)
        try:
            age = int(age_input)
            if age <= 0:
                print_message("Age must be greater than 0.", "error")
            else:
                return age
        except ValueError:
            print_message("Invalid input! Please enter numbers only.", "error")
# -----------------------------------------------


# Department screens

def show_add_department_screen():
    print_header("ADD DEPARTMENT")
    dept_name = input("Enter new department name: ")
    return dept_name

def show_department_selection_screen(department_names):
    print_header("SELECT DEPARTMENT")
    if not department_names:
        print_message("No departments exist yet. Please add one first.", "error")
        return None
    for i, name in enumerate(department_names, start=1):
        print(f"  {i}. {name}")
    print_divider()
    choice = input("Choose a department by number: ").strip()
    return choice

# Patient screens

def show_register_patient_screen():
    print_header("REGISTER PATIENT")
    name = input("Patient name: ")
    # هنا استخدمنا دالة الحماية بدل input العادية
    age = get_valid_age("Patient age: ") 
    record = input("Medical record (e.g. 'No known allergies'): ")
    return {
        "name": name,
        "age": age,
        "medical_record": record
    }

def show_search_patient_screen():
    print_header("SEARCH PATIENT")
    name = input("Enter patient name to search: ")
    return name

# Staff screen

def show_register_staff_screen():
    print_header("REGISTER STAFF")
    name = input("Staff name: ")
    # هنا استخدمنا دالة الحماية بدل input العادية
    age = get_valid_age("Staff age: ") 
    position = input("Staff position (e.g. 'Cardiologist'): ")
    return {
        "name": name,
        "age": age,
        "position": position
    }

# Hospital report screen

def show_hospital_report_screen(report_data):
    print_header(f"HOSPITAL REPORT: {report_data['hospital_name']}")
    print(f"Location: {report_data['location']}")
    print(f"Total Departments: {report_data['total_departments']}")
    print(f"Total Patients:    {report_data['total_patients']}")
    print(f"Total Staff:       {report_data['total_staff']}")
    
    if not report_data["departments"]:
        print("\nNo departments registered yet.")
        return
        
    for dept in report_data["departments"]:
        print(f"\n--- Department: {dept['name']} ---")
        print(f"  Patients ({len(dept['patients'])}):")
        if dept["patients"]:
            for line in dept["patients"]:
                print(f"    - {line}")
        else:
            print("    (no patients)")
            
        print(f"  Staff ({len(dept['staff'])}):")
        if dept["staff"]:
            for line in dept["staff"]:
                print(f"    - {line}")
        else:
            print("    (no staff)")
    print("=" * 50)

# Search results screen

def show_search_results_screen(search_name, results):
    if not results:
        print_message(f"No patient found matching '{search_name}'.", "error")
        return
    print_header(f"SEARCH RESULTS FOR '{search_name}'")
    for line in results:
        print(f"  {line}")

# Exit screen

def show_exit_screen():
    print_header("GOODBYE")
    print("Thank you for using the Hospital Management System!")



if __name__ == "__main__":
    print_welcome_screen()
    print_hospital_banner("City Hospital", "123 Main St")
    choice = show_main_menu()
    print_message(f"You chose option: {choice}", "info")
    if choice == "2":
        patient_data = show_register_patient_screen()
        print_message(f"You entered: {patient_data}", "success")
    show_exit_screen()