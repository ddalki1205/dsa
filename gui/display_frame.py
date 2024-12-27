from customtkinter import *
from PIL import Image, ImageTk
import heapq  # Assumed the hospital_queue is using heapq

class DisplayFrame(CTkFrame):
    SCALING = 1.5
    MAX_PATIENTS = 10  # Only show 10 patients
    MAX_PER_COLUMN = 5  # Max patients per column (for 2 columns)

    def __init__(self, parent, hospital_queue):
        super().__init__(parent.root, fg_color="white", bg_color="white")
        self.hospital_queue = hospital_queue
        self.parent = parent
        self.create_widgets()

    def create_widgets(self):
        # Title Frame
        self.title_frame = CTkFrame(self, fg_color="white")
        self.title_frame.pack(pady=10)

        # Hospital Logo
        self.logo_pil = Image.open("gui/images/hospital-logo.png")
        self.logo_pil = self.logo_pil.resize((90, 90))
        self.logo_img = ImageTk.PhotoImage(self.logo_pil)

        self.logo_label = CTkLabel(self.title_frame, image=self.logo_img, text="")
        self.logo_label.pack(side="left", padx=10)

        self.title_label = CTkLabel(self.title_frame, text="Hospital Waiting Room", text_color="#14375e", font=("Segoe UI", 50, "bold"))
        self.title_label.pack(pady=7)

        # Content Frame
        self.content_frame = CTkFrame(self, fg_color="white")
        self.content_frame.pack(fill="both", expand=True, padx=20, pady=10)

        # Now Preparing Frame (Left Side)
        self.now_preparing_frame = CTkFrame(self.content_frame, fg_color="white", width=500, height=540)
        self.now_preparing_frame.grid(row=0, column=0, sticky="w", padx=70, pady=0)
        self.now_preparing_frame.grid_propagate(False)

        self.now_preparing_label = CTkLabel(self.now_preparing_frame, text="IN LINE", text_color="#14375e", font=("SF Pro Display", 39))
        self.now_preparing_label.grid(row=0, column=0, columnspan=2, padx=20, pady=5)

        # Get patients from the hospital queue (priority order)
        patients = self.hospital_queue.get_patients()[:DisplayFrame.MAX_PATIENTS]  # Only get up to 10 patients
        
        # Generate display strings for the patient ids (replacing line_number with patient_id)
        preparing_numbers = [f"{patient.patient_id}" for patient in patients]

        # Divide the patients into two columns, with max 5 patients per column
        col_1 = "\n".join(preparing_numbers[:DisplayFrame.MAX_PER_COLUMN])
        col_2 = "\n".join(preparing_numbers[DisplayFrame.MAX_PER_COLUMN:])

        # Left Column (Top to Bottom)
        self.preparing_column_1 = CTkLabel(self.now_preparing_frame, text=col_1, text_color="black", font=("Segoe UI", 30), justify="left")
        self.preparing_column_1.grid(row=1, column=0, padx=10, pady=5)

        # Right Column (Top to Bottom)
        self.preparing_column_2 = CTkLabel(self.now_preparing_frame, text=col_2, text_color="black", font=("Segoe UI", 30), justify="left")
        self.preparing_column_2.grid(row=1, column=1, padx=10, pady=5)

        # Now Serving Frame (Right Side)
        self.now_serving_frame = CTkFrame(self.content_frame, fg_color="white")
        self.now_serving_frame.grid(row=0, column=1, sticky="e", padx=10)

        self.now_serving_label = CTkLabel(self.now_serving_frame, text="ATTENDING TO", text_color="green", font=("SF Pro Display", 50))
        self.now_serving_label.grid(row=0, column=0, padx=20, pady=5)

        # For now, the serving patient number is the first one in the heap (highest priority)
        if patients:
            serving_patient = patients[0]  # Highest priority patient (first in heap)
            self.serving_number_label = CTkLabel(self.now_serving_frame, text=f"{serving_patient.patient_id}", 
                                                 text_color="green", font=("Segoe UI", 92, "bold"))
            self.serving_number_label.grid(row=1, column=0, padx=20, pady=5)

        # Footer Frame
        self.footer_frame = CTkFrame(self, fg_color="white")
        self.footer_frame.pack(pady=10, side="bottom", fill="x")

        # Footer Text
        self.footer_label = CTkLabel(self.footer_frame, text="Public Medical Hospital", text_color="#14375e", font=("Segoe UI", 16), justify="center")
        self.footer_label.pack(padx=20)
