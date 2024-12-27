from customtkinter import *
from PIL import Image, ImageTk
import heapq  # Assuming hospital_queue uses heapq

class DisplayFrame(CTkFrame):
    SCALING = 1.5
    MAX_PATIENTS = 10  # Only show up to 10 patients
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

        self.title_label = CTkLabel(self.title_frame, text="Hospital Waiting Room", text_color="#14375e",
                                    font=("Segoe UI", 50, "bold"))
        self.title_label.pack(pady=7)

        # Content Frame
        self.content_frame = CTkFrame(self, fg_color="white")
        self.content_frame.pack(fill="both", expand=True, padx=20, pady=10)

        # Now Preparing Frame (Left Side)
        self.now_preparing_frame = CTkFrame(self.content_frame, fg_color="white", width=500, height=520)
        self.now_preparing_frame.grid(row=0, column=0, sticky="w", padx=70, pady=0)
        self.now_preparing_frame.grid_propagate(False)

        self.now_preparing_label = CTkLabel(self.now_preparing_frame, text="IN LINE", text_color="#14375e",
                                            font=("SF Pro Display", 39))
        self.now_preparing_label.grid(row=0, column=0, columnspan=2, padx=20, pady=5)

        # Now Serving Frame (Right Side)
        self.now_serving_frame = CTkFrame(self.content_frame, fg_color="white")
        self.now_serving_frame.grid(row=0, column=1, sticky="e", padx=5)

        self.now_serving_label = CTkLabel(self.now_serving_frame, text="ATTENDING TO", text_color="green",
                                          font=("SF Pro Display", 50))
        self.now_serving_label.grid(row=0, column=0, padx=20, pady=5)

        # Footer Frame
        self.footer_frame = CTkFrame(self, fg_color="white")
        self.footer_frame.pack(pady=10)

        self.footer_label = CTkLabel(self.footer_frame,
                                     text="@ 2024 Public Medical Hospital Institute. All Rights Reserved",
                                     text_color="#14375e", font=("Segoe UI", 16), justify="center")
        self.footer_label.pack(padx=20)

        # Login Button
        self.display_button = CTkButton(
            self,
            text="",
            command=self.switch_to_login,
            fg_color="#14375e",
            height=10000,
            width=60,
            bg_color="#14375e",
            anchor="s"
        )
        self.display_button.place(relx=0.97, rely=0.5, anchor="center")

    def update_content(self):
        # Clear existing widgets in Now Preparing and Now Serving frames
        for widget in self.now_preparing_frame.winfo_children():
            widget.destroy()

        for widget in self.now_serving_frame.winfo_children():
            widget.destroy()

        # Re-add titles
        self.now_preparing_label = CTkLabel(self.now_preparing_frame, text="IN LINE", text_color="#14375e",
                                            font=("SF Pro Display", 39))
        self.now_preparing_label.grid(row=0, column=0, columnspan=2, padx=20, pady=5)

        self.now_serving_label = CTkLabel(self.now_serving_frame, text="ATTENDING TO", text_color="green",
                                          font=("SF Pro Display", 50))
        self.now_serving_label.grid(row=0, column=0, padx=20, pady=5)

        # Get updated patient data
        patients = self.hospital_queue.get_patients()[:DisplayFrame.MAX_PATIENTS]  # Get up to 10 patients
        preparing_numbers = [f"{patient.patient_id}" for patient in patients]

        # Divide patients into two columns
        col_1 = "\n".join(preparing_numbers[:DisplayFrame.MAX_PER_COLUMN])
        col_2 = "\n".join(preparing_numbers[DisplayFrame.MAX_PER_COLUMN:])

        # Left Column
        self.preparing_column_1 = CTkLabel(self.now_preparing_frame, text=col_1, text_color="black",
                                           font=("Segoe UI", 30), justify="left")
        self.preparing_column_1.grid(row=1, column=0, padx=10, pady=5)

        # Right Column
        self.preparing_column_2 = CTkLabel(self.now_preparing_frame, text=col_2, text_color="black",
                                           font=("Segoe UI", 30), justify="left")
        self.preparing_column_2.grid(row=1, column=1, padx=10, pady=5)

        # Now Serving
        if patients:
            serving_patient = patients[0]  # Highest priority patient
            self.serving_number_label = CTkLabel(self.now_serving_frame, text=f"{serving_patient.patient_id}",
                                                 text_color="green", font=("Segoe UI", 92, "bold"))
            self.serving_number_label.grid(row=1, column=0, padx=20, pady=5)

    def on_show(self):
        self.update_content()

    def switch_to_login(self):
        self.parent.frame_manager.switch_to("login")