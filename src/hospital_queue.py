import heapq
from .patient import Patient

class HospitalQueue:
    """
    Manages the hospital's patient queue using a priority queue.
    """
    def __init__(self):
        self.queue = []
        self.counter = 0

    def add_patient(self, name, severity):
        """
        Add a patient to the queue, with an auto-incremented arrival time.
        """
        self.counter += 1
        patient = Patient(name, severity, self.counter)
        heapq.heappush(self.queue, (patient.get_priority(), patient))
        print(f"Patient added: {patient}")

    def remove_patient(self):
        """
        Remove and attend to the patient with the highest priority.
        """
        if not self.queue:
            print("Error: No patients in the queue.")
            return None

        _, attended = heapq.heappop(self.queue)
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
        for i, (_, patient) in enumerate(self.queue):
            if patient.name == name:
                return patient
        print(f"Error: Patient '{name}' not found.")
        return None

    def _reinsert_patient(self, patient, new_severity):
        """
        Helper function to update the severity and reinsert a patient into the queue.
        """
        # Remove old entry
        self.queue = [(priority, p) for priority, p in self.queue if p != patient]
        heapq.heapify(self.queue)

        # Update severity and reinsert
        patient.severity = new_severity
        heapq.heappush(self.queue, (patient.get_priority(), patient))
        print(f"Updated severity for {patient.name} to {new_severity}")

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
