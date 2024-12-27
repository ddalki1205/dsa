from customtkinter import *
import random

class AdminFrame(CTkFrame):
    def __init__(self, parent, hospital_queue):
        super().__init__(parent.root, fg_color="white", bg_color="white")
        self.parent = parent
        self.hospital_queue = hospital_queue

        # Adding initial patients
        self._add_initial_patients()

        # Popup frame to edit patient severity
        self.popup_frame = None

        # Create header frame
        self.header_frame = CTkFrame(self)
        self.header_frame.pack(fill="x", padx=20, pady=5)
        self._create_table_headers()

        # Create a scrollable frame for the table
        self.scrollable_frame = CTkScrollableFrame(self)
        self.scrollable_frame.pack(fill="both", expand=True, padx=20, pady=20)

        # Update table with current data
        self._update_table()

    def _add_initial_patients(self):
        """Adds some sample patients to the queue."""
        # Sample names for random patient generation
        names = [
            "Jackson", "James", "Sophia", "Liam", "Emma", "Oliver", "Ava", 
            "Lucas", "Mia", "Noah", "Isabella", "Elijah", "Zoe", "Aiden", "Amelia"
        ]

        # Randomly generate patients and add them to the hospital queue
        for name in random.sample(names, 15):  # Ensure unique names
            severity = random.randint(1, 10)  # Random severity between 1 and 10
            self.hospital_queue.add_patient(name=name, severity=severity)

    def _create_table_headers(self):
        """Creates the header row for the patient table."""
        headers = ["Line Number", "Name", "Severity", "Arrival Time", "Actions"]
        for idx, header in enumerate(headers):
            header_label = CTkLabel(self.header_frame, text=header, width=150, anchor="w")
            header_label.grid(row=0, column=idx, padx=10, pady=5)

    def _edit_patient_severity(self, patient):
        """Opens a popup to edit the severity of a patient."""
        # Close any existing popup
        if self.popup_frame is not None:
            self.popup_frame.place_forget()

        self.popup_frame = CTkFrame(self, fg_color="gray", corner_radius=10, width=400, height=200)
        self.popup_frame.place(relx=0.5, rely=0.5, anchor="center")

        # Create input form for new severity
        self._create_severity_form(patient)

    def _create_severity_form(self, patient):
        """Creates a form in the popup to input new severity."""
        def submit_new_severity():
            new_severity = self.severity_input.get()
            if new_severity.isdigit():
                self.hospital_queue.update_severity(patient.name, int(new_severity))
                self._update_table()
                self.popup_frame.place_forget()
            else:
                print("Please enter a valid severity value")

        # Create popup form fields
        CTkLabel(self.popup_frame, text=f"Enter new severity for {patient.name}:").pack(pady=10)
        self.severity_input = CTkEntry(self.popup_frame)
        self.severity_input.pack(pady=10)
        CTkButton(self.popup_frame, text="Submit", command=submit_new_severity).pack(pady=10)
        CTkButton(self.popup_frame, text="X", width=30, height=30, command=self.popup_frame.place_forget).place(relx=0.95, rely=0.05)

    def _attend_to_patient(self):
        """Attends to the first patient in the queue."""
        patients = self.hospital_queue.get_patients()
        if patients:
            first_patient = patients[0]
            print(f"Attending to {first_patient.name} (Severity: {first_patient.severity})")
            self.hospital_queue.remove_patient()
            self._update_table()

    def _update_table(self):
        """Updates the patient table with the current queue data."""
        # Clear existing rows in scrollable frame
        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()

        # Add patient rows dynamically
        for idx, patient in enumerate(self.hospital_queue.get_patients()):
            self._create_patient_row(idx, patient)

    def _create_patient_row(self, idx, patient):
        """Creates a row for a patient in the table."""
        patient_frame = CTkFrame(self.scrollable_frame)
        patient_frame.pack(fill="x", padx=20, pady=5)

        # Populate the row with patient data
        self._add_patient_labels(patient_frame, patient)

        # Add action buttons (Attend and Edit)
        self._add_patient_buttons(patient_frame, patient, idx)

    def _add_patient_labels(self, patient_frame, patient):
        """Adds labels for the patient information in a row."""
        CTkLabel(patient_frame, text=str(patient.line_number), width=150, anchor="w").grid(row=0, column=0, padx=10, pady=5)
        CTkLabel(patient_frame, text=patient.name, width=150, anchor="w").grid(row=0, column=1, padx=10, pady=5)
        CTkLabel(patient_frame, text=str(patient.severity), width=150, anchor="w").grid(row=0, column=2, padx=10, pady=5)
        CTkLabel(patient_frame, text=patient.arrival_time, width=150, anchor="w").grid(row=0, column=3, padx=10, pady=5)

    def _add_patient_buttons(self, patient_frame, patient, idx):
        """Adds the 'Attend' and 'Edit' buttons for each patient."""
        # Add "Attend" button for the first patient in the queue
        if idx == 0:
            attend_button = CTkButton(patient_frame, text="Attend", command=self._attend_to_patient)
            attend_button.grid(row=0, column=4, padx=10, pady=5)

        # Add "Edit" button for all patients
        edit_button = CTkButton(patient_frame, text="Edit", command=lambda p=patient: self._edit_patient_severity(p))
        edit_button.grid(row=0, column=5, padx=10, pady=5)
