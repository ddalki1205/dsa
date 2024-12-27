import customtkinter as ctk
from PIL import Image, ImageTk

class HospitalDisplayApp(ctk.CTk):
    SCALING = 1.5
    MAX_PER_COLUMN = 10

    def __init__(self):
        super().__init__()
        self.title("Hospital Waiting Room Display")
        self.configure(fg_color="white")

        screen_w = self.winfo_screenwidth()
        screen_h = self.winfo_screenheight()

        root_w = int(screen_w // HospitalDisplayApp.SCALING)
        root_h = int(screen_h // HospitalDisplayApp.SCALING)

        root_resolution = f"{root_w}x{root_h}"

        center_x = int((screen_w - root_w) // 2)
        center_y = int((screen_h - root_h) // 2)

        geometry = f"{root_resolution}+{center_x}+{center_y}"

        self.geometry(geometry)
        self.create_widgets()

    def create_widgets(self):
#-----------------------------------------------------------------------------------------------------

        # Title Frame
        self.title_frame = ctk.CTkFrame(self, fg_color="white")
        self.title_frame.pack(pady=10)

        # Hospital Logo
        self.logo_pil = Image.open("gui/images/hospital-logo.png") 
        self.logo_pil = self.logo_pil.resize((90, 90))
        self.logo_img = ImageTk.PhotoImage(self.logo_pil)

        self.logo_label = ctk.CTkLabel(self.title_frame, image=self.logo_img, text="")
        self.logo_label.pack(side="left", padx=10)

        self.title_label = ctk.CTkLabel(self.title_frame, text="Hospital Waiting Room", text_color="#14375e", font=("Segoe UI", 50, "bold"))
        self.title_label.pack(pady=7)

        # Content Frame
        self.content_frame = ctk.CTkFrame(self, fg_color="white")
        self.content_frame.pack(fill="both", expand=True, padx=20, pady=10)

#-----------------------------------------------------------------------------------------------------

        # Now Preparing Frame (Left Side)
        self.now_preparing_frame = ctk.CTkFrame(self.content_frame, fg_color="white", width=500, height=540)
        self.now_preparing_frame.grid(row=0, column=0, sticky="w", padx=70, pady=0)

        # To make the frame honor the fixed dimensions:
        self.now_preparing_frame.grid_propagate(False)

        self.now_preparing_label = ctk.CTkLabel(self.now_preparing_frame, text="IN LINE", text_color="#14375e", font=("SF Pro Display", 39))
        self.now_preparing_label.grid(row=0, column=0, columnspan=2, padx=20, pady=5)

        #dummy data
        preparing_numbers = ["112", "114", "115", "117", "118", "120", "122", "123", "124", "126", 
                             "128", "130", "131", "133", "134", "135", "136", "137", "138", "139"]

        # Divide numbers into columns
        col_1 = "\n".join(preparing_numbers[:HospitalDisplayApp.MAX_PER_COLUMN])
        col_2 = "\n".join(preparing_numbers[HospitalDisplayApp.MAX_PER_COLUMN:])

        # Left Column
        self.preparing_column_1 = ctk.CTkLabel(self.now_preparing_frame, text=col_1, text_color="black", font=("Segoe UI", 30), justify="left")
        self.preparing_column_1.grid(row=1, column=0, padx=10, pady=5)

        # Right Column
        self.preparing_column_2 = ctk.CTkLabel(self.now_preparing_frame, text=col_2, text_color="black", font=("Segoe UI", 30), justify="left")
        self.preparing_column_2.grid(row=1, column=1, padx=10, pady=5)

#-----------------------------------------------------------------------------------------------------

        # Now Serving Frame (Right Side)
        self.now_serving_frame = ctk.CTkFrame(self.content_frame, fg_color="white")
        self.now_serving_frame.grid(row=0, column=1, sticky="e", padx=10)

        self.now_serving_label = ctk.CTkLabel(self.now_serving_frame, text="NOW SERVING", text_color="green", font=("SF Pro Display", 50),)
        self.now_serving_label.grid(row=0, column=0, padx=20, pady=5)

        self.serving_number_label = ctk.CTkLabel(self.now_serving_frame, text="105", text_color="green", font=("Segoe UI", 92, "bold"),)
        self.serving_number_label.grid(row=1, column=0, padx=20, pady=5)

#-----------------------------------------------------------------------------------------------------

        # Footer Frame
        self.footer_frame = ctk.CTkFrame(self, fg_color="white")
        self.footer_frame.pack(pady=10, side="bottom", fill="x")

        # Footer Text
        self.footer_label = ctk.CTkLabel(self.footer_frame, text="Public Medical Hospital", text_color="#14375e", font=("Segoe UI", 16), justify="center")
        self.footer_label.pack(padx=20)

if __name__ == "__main__":
    app = HospitalDisplayApp()
    app.mainloop()