import heapq
from .patient import Patient
from datetime import datetime

class HospitalQueue:
    """
    Manages the hospital's patient queue using a priority queue (min-heap).
    """
    def __init__(self):
        self.queue = []  # The internal priority queue

    def add_patient(self, name, severity):
        """
        Add a patient to the queue, with an auto-incremented arrival time.
        After adding the patient, assign their line number based on their position in the queue.
        """
        arrival_time = datetime.now()
        patient = Patient(name, severity, arrival_time, 0)  # Initial line_number is set to 0 temporarily
        heapq.heappush(self.queue, (patient.get_priority(), patient))
        self._assign_line_numbers()  # Assign line numbers based on the queue position
        print(f"Patient added: {patient}")

    def remove_patient(self):
        """
        Remove and attend to the patient with the highest priority (lowest severity).
        """
        if not self.queue:
            print("Error: No patients in the queue.")
            return None

        _, attended = heapq.heappop(self.queue)
        self._assign_line_numbers()  # Reassign line numbers after removal
        print(f"Attending to: {attended}")
        return attended

    def update_severity(self, name, new_severity):
        """
        Update the severity level of a patient in the queue.
        """
        patient = self.find_patient(name)
        if patient:
            self._reinsert_patient(patient, new_severity)

    def find_patient(self, name):
        """
        Find a patient by name. Return the patient or None.
        """
        for _, patient in self.queue:
            if patient.name == name:
                return patient
        print(f"Error: Patient '{name}' not found.")
        return None

    def display_queue(self):
        """
        Display the current queue, sorted by priority.
        """
        if not self.queue:
            print("No patients in the queue.")
            return

        print("Current Queue (by priority):")
        temp_queue = sorted(self.queue, key=lambda x: x[0])  # Sort by priority
        for _, patient in temp_queue:
            print(f"\t{patient}")

    def get_patients(self) -> list:
        """
        Returns an array of patients in order based on highest to lowest priority
        """
        if not self.queue:
            return None
        temp_queue = sorted(self.queue, key=lambda x: x[0])
        patients = []
        for _, patient in temp_queue:
            patients.append(patient)
        return patients
    
    def _reinsert_patient(self, patient, new_severity):
        """
        Helper function to update the severity and reinsert a patient into the queue.
        """
        # Remove old entry by filtering out the patient
        self.queue = [(priority, p) for priority, p in self.queue if p != patient]
        heapq.heapify(self.queue)

        # Update severity and reinsert
        patient.severity = new_severity
        heapq.heappush(self.queue, (patient.get_priority(), patient))
        self._assign_line_numbers()  # Reassign line numbers after re-insertion
        print(f"Updated severity for {patient.name} to {new_severity}")

    def _assign_line_numbers(self):
        """
        Helper function to assign line numbers to patients based on their position in the queue.
        """
        for i, (_, patient) in enumerate(self.queue):
            patient.line_number = i + 1  # Assign line number (1-based index)