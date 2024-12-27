from customtkinter import *
from src.hospital_queue import HospitalQueue


# Initialize hospital queue
hospital = HospitalQueue()
hospital.add_patient("Jackson", 2)
hospital.add_patient("James", 6)

# Initialize the main window
root = CTk()
root.geometry("800x600")

# Frame for the table header
header_frame = CTkFrame(root)
header_frame.pack(fill="x", padx=20, pady=5)

headers = ["Line Number", "Name", "Severity", "Arrival Time", "Actions"]
for idx, header in enumerate(headers):
    header_label = CTkLabel(header_frame, text=header, width=150, anchor="w")
    header_label.grid(row=0, column=idx, padx=10, pady=5)

# Function to edit patient severity (this is now inside the frame)
def edit_patient_severity(patient):
    def submit_new_severity():
        new_severity = severity_input.get()
        if new_severity.isdigit():
            hospital.update_severity(patient.name, int(new_severity))
            update_table()  # Update table with new severity
            popup_frame.place_forget()  # Close the popup frame
        else:
            print("Please enter a valid severity value")

    # Create a frame that will act as a modal popup
    popup_frame = CTkFrame(root, fg_color="gray", corner_radius=10, width=400, height=200)
    popup_frame.place(relx=0.5, rely=0.5, anchor="center")  # Place at the center

    # Create the input form inside the popup frame
    CTkLabel(popup_frame, text=f"Enter new severity for {patient.name}:").pack(pady=10)
    severity_input = CTkEntry(popup_frame)
    severity_input.pack(pady=10)
    CTkButton(popup_frame, text="Submit", command=submit_new_severity).pack(pady=10)

# Function to attend to the first patient in the queue
def attend_to_patient():
    if hospital.get_patients():
        first_patient = hospital.get_patients()[0]
        print(f"Attending to {first_patient.name} (Severity: {first_patient.severity})")
        hospital.remove_first_patient()
        update_table()  # Update the table after attending to the first patient

# Function to update the table with patient data
def update_table():
    # Clear the previous table rows
    for widget in table_frame.winfo_children():
        widget.destroy()

    # Add patient rows dynamically
    for idx, patient in enumerate(hospital.get_patients()):
        patient_frame = CTkFrame(table_frame)
        patient_frame.pack(fill="x", padx=20, pady=5)

        line_number = patient.line_number # Dynamic line number
        name = patient.name
        severity = patient.severity
        arrival_time = patient.arrival_time

        CTkLabel(patient_frame, text=str(line_number), width=150, anchor="w").grid(row=0, column=0, padx=10, pady=5)
        CTkLabel(patient_frame, text=name, width=150, anchor="w").grid(row=0, column=1, padx=10, pady=5)
        CTkLabel(patient_frame, text=str(severity), width=150, anchor="w").grid(row=0, column=2, padx=10, pady=5)
        CTkLabel(patient_frame, text=arrival_time, width=150, anchor="w").grid(row=0, column=3, padx=10, pady=5)

        # If this is the first patient, display the "Attend" and "Edit" buttons
        if idx == 0:  # Only show buttons for the first patient
            attend_button = CTkButton(patient_frame, text="Attend", command=attend_to_patient)
            attend_button.grid(row=0, column=4, padx=10, pady=5)

        edit_button = CTkButton(patient_frame, text="Edit", command=lambda p=patient: edit_patient_severity(p))
        edit_button.grid(row=0, column=5, padx=10, pady=5)

# Frame to hold the table rows
table_frame = CTkFrame(root)
table_frame.pack(fill="both", expand=True, padx=20, pady=20)

# Update the table initially
update_table()

# Start the Tkinter main loop
root.mainloop()
