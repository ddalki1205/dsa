#from src.Patient import Patient

import heapq

class Patient:
    '''
    params:
    - name: str = name of the patient
    - severity: int = starting with 1 indicating low severity, e.g, low priority
    - arrival_time: int = global counter starting with 0 from hospital queue
    '''
    def __init__(self, name: str, severity: int, arrival_time: int):
        self.name: str = name
        self.severity: int = severity
        self.arrival_time: int = arrival_time

    def patient_priority(self) -> tuple:
        '''
        Returns the priority of the patient as a tuple.
        
        Priority is determined by:
        - Negative severity (higher severity is higher priority)
        - Arrival time (earlier arrivals are higher priority for the same severity)
        '''
        return (-self.severity, self.arrival_time)

    def __str__(self):
        return f"{self.name} (Severity: {self.severity}, Arrival: {self.arrival_time})"
    
class HospitalQueue:
    '''
    A class to manage a hospital patient queue using a priority queue (min-heap).
    
    Attributes:
    - queue: list = The internal priority queue to store patients
    - counter: int = A global counter for arrival times to ensure correct ordering
    '''
    def __init__(self):
        self.queue = []  
        self.counter = 0  # arrival order

    def add_patient(self, name, severity):
        '''
        Adds a new patient to the queue.

        params:
        - name: str = Name of the patient
        - severity: int = Severity level (1-10), where 1 is low severity

        The patient is assigned an arrival time based on the current counter.
        '''
        self.counter += 1
        patient = Patient(name, severity, self.counter)
        heapq.heappush(self.queue, (patient.patient_priority(), patient))
        print(f"Patient added: {patient}")

    def remove_patient(self):
        '''
        Removes and returns the patient with the highest priority (lowest severity value and earliest arrival time).
        
        If the queue is empty, prints an error message and returns None.
        '''
        if not self.queue:
            print("Error: No patients in the queue.")
            return None
        
        _, attended = heapq.heappop(self.queue)
        print(f"Attending to: {attended}")
        return attended

    def update_severity(self, name, new_severity):
        '''
        Updates the severity level of a specific patient in the queue.

        params:
        - name: str = Name of the patient whose severity needs updating
        - new_severity: int = The new severity level (1-10)
        
        If the patient is found:
        - Removes them from the queue
        - Updates their severity
        - Reinserts them into the queue with the new priority

        If the patient is not found, prints an error message.
        '''
        found = None
        for i, (_, patient) in enumerate(self.queue):
            if patient.name == name:
                found = (i, patient)
                break

        if found:
            index, patient = found
            del self.queue[index]
            heapq.heapify(self.queue)
            patient.severity = new_severity 
            heapq.heappush(self.queue, (patient.patient_priority(), patient))  # changing severity
            print(f"Updated severity for {name} to {new_severity}")
        else:
            print(f"Error: Patient '{name}' not found.")

    def display_queue(self):
        '''
        Displays the current queue, sorted by priority for readability.

        The queue is temporarily sorted (not modifying the actual heap structure),
        with patients displayed in order of decreasing priority.
        '''
        print("Current Queue (by priority):")
        temp_queue = list(self.queue)
        sorted_queue = sorted(temp_queue, key=lambda x: x[0])  # Sort by priority
        for _, patient in sorted_queue:
            print(f"\t{patient}")

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