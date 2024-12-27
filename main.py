import heapq

# === Manage patient info
class Patient:
    def __init__(self, name, severity, arrival_time):
        self.name = name
        self.severity = severity
        self.arrival_time = arrival_time

    def __str__(self):
        return f"{self.name} (Severity: {self.severity}, Arrival: {self.arrival_time})"

def patient_priority(patient):
    # 1 = low severe, low priority
    # arrived earlier is prioritized if patients have same severity
    return ({patient.severity * -1}, patient.arrival_time)

# === Manage queue
class HospitalQueue:
    def __init__(self):
        self.queue = []  
        self.counter = 0  # arrival order

    def add_patient(self, name, severity):
        self.counter += 1
        patient = Patient(name, severity, self.counter)
        heapq.heappush(self.queue, (patient_priority(patient), patient))
        print(f"Patient added: {patient}")

    def remove_patient(self):
        if not self.queue:
            print("Error: No patients in the queue.")
            return None
        x, attended = heapq.heappop(self.queue)
        print(f"Attending to: {attended}")
        return attended

    def update_severity(self, name, new_severity):
        # Find patient in the queue
        found = None
        for i, (x, patient) in enumerate(self.queue):
            if patient.name == name:
                found = (i, patient)
                break

        if found:
            index, patient = found
            del self.queue[index]
            heapq.heapify(self.queue)
            patient.severity = new_severity 
            heapq.heappush(self.queue, (patient_priority(patient), patient))  # changing severity
            print(f"Updated severity for {name} to {new_severity}")
        else:
            print(f"Error: Patient '{name}' not found.")

    def display_queue(self):
        print("Current Queue:")
        for x, patient in sorted(self.queue):  # sorted  in priority order
            print(f"  {patient}")


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
