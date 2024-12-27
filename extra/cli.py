from src.hospital_queue import HospitalQueue

'''

TERMINAL BASED PROGRAM NOT IN USED (OLD VERSION OF THE PROGRAM BEING REPLACED WITH A GUI)

'''

def display_menu():
    """
    Display the main menu options.
    """
    print("\nHospital Queue Management")
    print("1. Add Patient")
    print("2. Remove Patient (Attend)")
    print("3. Update Severity")
    print("4. Display Queue")
    print("5. Exit")

def handle_choice(queue, choice):
    """
    Handle the user's menu choice.
    """
    if choice == '1':
        return handle_add_patient(queue)
    elif choice == '2':
        return handle_remove_patient(queue)
    elif choice == '3':
        return handle_update_severity(queue)
    elif choice == '4':
        queue.display_queue()
        return True
    elif choice == '5':
        print("Exiting the system.")
        return False
    else:
        print("Invalid choice. Please try again.")
        return True

def handle_add_patient(queue):
    """
    Add a patient to the queue.
    """
    name = input("Enter patient name: ")
    severity = int(input("Enter severity level (1-10): "))
    queue.add_patient(name, severity)
    return True

def handle_remove_patient(queue):
    """
    Remove a patient from the queue.
    """
    queue.remove_patient()
    return True

def handle_update_severity(queue):
    """
    Update a patient's severity level.
    """
    name = input("Enter patient name to update: ")
    new_severity = int(input("Enter new severity level (1-10): "))
    queue.update_severity(name, new_severity)
    return True

def main():
    """
    Main function to manage the hospital queue system.
    """
    queue = HospitalQueue()
    running = True

    while running:
        display_menu()
        choice = input("Enter your choice: ")
        running = handle_choice(queue, choice)

if __name__ == "__main__":
    main()