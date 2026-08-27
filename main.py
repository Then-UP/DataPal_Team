from cli_ui import *
from hospital import Hospital
from department import Department
from patient import Patient
from staff import Staff
from file_io import save_hospital_data, load_hospital_data

def main():
    print_welcome_screen()
    
    
    hospital = load_hospital_data()
    if not hospital:
        hospital = Hospital("City Hospital", "123 Main St")
        
    print_hospital_banner(hospital.name, hospital.location)

    
    while True:
        choice = show_main_menu()
        
        try:
            if choice == "1":
                dept_name = show_add_department_screen()
                hospital.add_department(Department(dept_name))
                print_message("Department added successfully!", "success")
                
            elif choice == "2":
                dept_names = [d.name for d in hospital.departments]
                dept_choice = show_department_selection_screen(dept_names)
                if dept_choice:
                    selected_dept = hospital.departments[int(dept_choice) - 1]
                    p_data = show_register_patient_screen()
                    selected_dept.add_patient(Patient(p_data["name"], int(p_data["age"]), p_data["medical_record"]))
                    print_message("Patient registered successfully!", "success")
                    
            elif choice == "3":
                dept_names = [d.name for d in hospital.departments]
                dept_choice = show_department_selection_screen(dept_names)
                if dept_choice:
                    selected_dept = hospital.departments[int(dept_choice) - 1]
                    s_data = show_register_staff_screen()
                    selected_dept.add_staff(Staff(s_data["name"], int(s_data["age"]), s_data["position"]))
                    print_message("Staff registered successfully!", "success")
                    
            elif choice == "4":
                search_name = show_search_patient_screen()
                results = hospital.search_patient_by_name(search_name)
                formatted = [f"{p.view_info()} | Dept: {d}" for p, d in results]
                show_search_results_screen(search_name, formatted)
                
            elif choice == "5":
                hospital.generate_report()
                
            elif choice == "6":
                save_hospital_data(hospital)
               
            elif choice == "0":
               
                save_hospital_data(hospital) 
                show_exit_screen()
                break
                
            else:
                print_message("Invalid option, please choose from the menu.", "error")
                

        except ValueError as e:
            print_message(f"Value Error: {e}", "error")
        except TypeError as e:
            print_message(f"Type Error: {e}", "error")
        except IndexError:
            print_message("Invalid selection! Please choose a correct number.", "error")
        except Exception as e:
            print_message(f"An unexpected error occurred: {e}", "error")

if __name__ == "__main__":
    main()