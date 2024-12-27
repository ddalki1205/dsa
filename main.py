from src.hospital_queue import HospitalQueue

queue = HospitalQueue()

while True:
    print("\nHospital Queue Management")
    print("1. Add Patient")
    print("2. Remove Patient (Attend)")
    print("3. Update Severity")
    print("4. Display Queue")
    print("5. Exit")
    
    choice = input("Enter your choice: ")

    if choice == '1':
        name = input("Enter patient name: ")
        severity = int(input("Enter severity level (1-10): "))
        queue.add_patient(name, severity)

    elif choice == '2':
        queue.remove_patient()

    elif choice == '3':
        name = input("Enter patient name to update: ")
        new_severity = int(input("Enter new severity level (1-10): "))
        queue.update_severity(name, new_severity)

    elif choice == '4':
        queue.display_queue()

    elif choice == '5':
        print("Exiting the system.")
        break

    else:
        print("Invalid choice. Please try again.")