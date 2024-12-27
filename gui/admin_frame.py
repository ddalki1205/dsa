from CTkTable import *
from customtkinter import *
from ..modules.hospital_queue import HospitalQueue

hospital = HospitalQueue()
hospital.add_patient("Jackson", 2)
hospital.add_patient("James", 6)

root = CTk() # configure this please

data_table = []
headers = ["Line Number", "Name", "Severity", "Edit"]
data_table.append(headers)

patients = None # get the patients from where
for patient in patients:
    line_number, name, severity = patient.get_data()
    edit = None # create button to remove patient or edit their severity here
    row = [line_number, name, severity, edit]
    data_table.append(row)

CTkTable(
    root, 
    row=len(data_table),
    column=len(headers), 
    values=data_table,
    bg_color="#010409",
    fg_color="#010409",
    header_color="#0a0c10",
    colors=["#0b0f14", "#151B23"],
    justify="left",
    orientation="horizontal",
    corner_radius=7,
).pack(expand=True, fill="both", padx=20, pady=20)

root.mainloop()