from customtkinter import *
from PIL import Image, ImageTk

class LoginFrame(CTkFrame):
    ADMIN_USER = "admin"
    ADMIN_PASSWORD = "admin"
    
    def __init__(self, parent):
        super().__init__(parent.root, fg_color="white", bg_color="white")
        self.parent = parent

        self.create_widgets()

    def create_widgets(self):
        # log in frame
        self.main_frame = CTkFrame(self, fg_color="white")
        self.main_frame.pack(side="left", padx=200)

        self.display_button = CTkButton(
            self,
            text="D\nI\nS\nP\nL\nA\nY",
            command=self.switch_to_display,
            fg_color="#14375e",
            bg_color="#14375e",
        )
        self.display_button.pack(side="left", fill="both", expand=True)

        # logo frame
        self.logo_frame = CTkFrame(self.main_frame, fg_color="white")
        self.logo_frame.pack(side="left", padx=0)

        self.logo_label = CTkLabel(
            self.logo_frame,
            image = CTkImage(
                light_image=Image.open(f"gui/images/hospital-logo.png"),
                size=(350, 350)
            ), 
            text="", fg_color="white"
        )
        self.logo_label.pack(side="left", pady=0)

        # login form frame
        self.login_form = CTkFrame(self.main_frame, fg_color="white")
        self.login_form.pack(side="left", padx=20, anchor="w")

        # Title
        self.title_label = CTkLabel(self.login_form, text="Log In", text_color="#14375e", bg_color="white", width=20, font=("SF Pro Display", 100))
        self.title_label.pack(pady=50, anchor="w")

        # Username frame
        self.username_frame = CTkFrame(self.login_form, bg_color="white", fg_color="white")
        self.username_frame.pack(pady=10, anchor="w")

        # Username label and entry
        self.user_label = CTkLabel(self.username_frame, text="Username:", text_color="black", bg_color="white", font=("Segoe UI", 16))
        self.user_label.pack(side="left", padx=5)

        self.user_entry = CTkEntry(self.username_frame, text_color="black", bg_color="white", fg_color="white", font=("Segoe UI", 16), width=250)
        self.user_entry.pack(side="left", padx=5)

        # Password frame
        self.password_frame = CTkFrame(self.login_form, bg_color="white", fg_color="white")
        self.password_frame.pack(pady=5, anchor="w")

        # Password label and entry
        self.password_label = CTkLabel(self.password_frame, text="Password:", text_color="black", bg_color="white", font=("Segoe UI", 16))
        self.password_label.pack(side="left", padx=5)

        self.password_entry = CTkEntry(self.password_frame, text_color="black", bg_color="white", fg_color="white", font=("Segoe UI", 16), width=250, show="*")
        self.password_entry.pack(side="left", padx=9)

        # Error label
        self.error_label = CTkLabel(self.login_form, text="", bg_color="white", font=("Segoe UI", 12), text_color="red")
        self.error_label.pack(pady=5, anchor="w")

        # Buttons
        login_btn = CTkButton(self.login_form, text="Log In", font=("Segoe UI", 20), width=180, height=15, border_spacing=10, command=self.login_confirm)
        exit_btn = CTkButton(self.login_form, text="Exit", font=("Segoe UI", 20), width=180, height=15, border_spacing=10, command=self.master.quit)

        login_btn.pack(padx=2, pady=5, anchor="w")
        exit_btn.pack(padx=2, pady=5, anchor="w")

    def switch_to_display(self):
        self.parent.frame_manager.switch_to("display")

    def login_confirm(self):
        username = self.user_entry.get()
        password = self.password_entry.get()

        if username == self.ADMIN_USER and password == self.ADMIN_PASSWORD:
            self.error_label.configure(text="", text_color="green")
            print("Login successful")
            self.parent.frame_manager.switch_to("admin")
            self.clear_form()
        else:
            self.error_label.configure(text="Invalid username or password", text_color="red")

    def clear_form(self):
        """Clear the username, password, and error label."""
        self.user_entry.delete(0, 'end')
        self.password_entry.delete(0, 'end')
        self.error_label.configure(text="")