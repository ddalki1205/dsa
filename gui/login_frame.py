import customtkinter as ctk
from PIL import Image, ImageTk

class LoginFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent.root, fg_color="white", bg_color="white")
        self.parent = parent

        self.create_widgets()

    def create_widgets(self):
        # log in frame
        self.main_frame = ctk.CTkFrame(self, fg_color="white")
        self.main_frame.pack(side="left", padx=200)

        # logo frame
        self.logo_frame = ctk.CTkFrame(self.main_frame, fg_color="white")
        self.logo_frame.pack(side="left", padx=0)

        # Logo image (use Pillow to load the image)
        self.logo_pil = Image.open("app/images/hospital-logo.png")
        self.logo_pil = self.logo_pil.resize((350, 350))
        self.logo_img = ImageTk.PhotoImage(self.logo_pil)

        self.logo_label = ctk.CTkLabel(self.logo_frame, image=self.logo_img, text="", fg_color="white")
        self.logo_label.pack(side="left", pady=0)

        # login form frame
        self.login_form = ctk.CTkFrame(self.main_frame, fg_color="white")
        self.login_form.pack(side="left", padx=20, anchor="w")

        # Title
        self.title_label = ctk.CTkLabel(self.login_form, text="Log In", text_color="#14375e", bg_color="white", width=20, font=("SF Pro Display", 100))
        self.title_label.pack(pady=50, anchor="w")

        # Username frame
        self.username_frame = ctk.CTkFrame(self.login_form, bg_color="white", fg_color="white")
        self.username_frame.pack(pady=10, anchor="w")

        # Username label and entry
        self.id_label = ctk.CTkLabel(self.username_frame, text="Username:", text_color="black", bg_color="white", font=("Segoe UI", 16))
        self.id_label.pack(side="left", padx=5)

        self.id_entry = ctk.CTkEntry(self.username_frame, text_color="black", bg_color="white", fg_color="white", font=("Segoe UI", 16), width=250)
        self.id_entry.pack(side="left", padx=5)

        # Password frame
        self.password_frame = ctk.CTkFrame(self.login_form, bg_color="white", fg_color="white")
        self.password_frame.pack(pady=5, anchor="w")

        # Password label and entry
        self.password_label = ctk.CTkLabel(self.password_frame, text="Password:", text_color="black", bg_color="white", font=("Segoe UI", 16))
        self.password_label.pack(side="left", padx=5)

        self.password_entry = ctk.CTkEntry(self.password_frame, text_color="black", bg_color="white", fg_color="white", font=("Segoe UI", 16), width=250, show="*")
        self.password_entry.pack(side="left", padx=9)

        # Error label
        self.error_label = ctk.CTkLabel(self.login_form, text="", bg_color="white", font=("Segoe UI", 12), text_color="red")
        self.error_label.pack(pady=5, anchor="w")

        # Buttons
        login_btn = ctk.CTkButton(self.login_form, text="Log In", font=("Segoe UI", 20), width=180, height=15, border_spacing=10, command=self.login_confirm)
        exit_btn = ctk.CTkButton(self.login_form, text="Exit", font=("Segoe UI", 20), width=180, height=15, border_spacing=10, command=self.master.quit)

        login_btn.pack(padx=2, pady=5, anchor="w")
        exit_btn.pack(padx=2, pady=5, anchor="w")

    def login_confirm(self):
        pass