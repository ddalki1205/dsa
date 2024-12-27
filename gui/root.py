import customtkinter as ctk
import ctypes

from .utils.frame_manager import FrameManager

from .admin_frame import AdminFrame
from .login_frame import LoginFrame
from .display_frame import DisplayFrame

# -----------------------------------------------------
#
# Root Window with configuration settings
#
# -----------------------------------------------------

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

class RootWindow:
    appid = 'arbitrary.string'
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(appid)
    
    def __init__(self, hospital_queue):
        self.hospital_queue = hospital_queue
        self.root = ctk.CTk()

        self.root.title("Hospital Kiosk")
        self.root.iconbitmap('gui/images/hospital-logo.ico')

        self.frame_manager = FrameManager(self.root)

        self.root.geometry(RootWindow.CenterWindowToDisplay(self.root, 1200, 700, self.root._get_window_scaling()))
        self.init_frames()
    
    @staticmethod
    def CenterWindowToDisplay(Screen: ctk.CTk, width: int, height: int, scale_factor: float = 1.0):
        """
        Centers the window to the main display/monitor
        
        Thanks to HyperNylium for the function!
        """
        screen_width = Screen.winfo_screenwidth()
        screen_height = Screen.winfo_screenheight()
        x = int(((screen_width/2) - (width/2)) * scale_factor)
        y = int(((screen_height/2) - (height/1.8)) * scale_factor)
        return f"{width}x{height}+{x}+{y}"

    def init_frames(self):
        self.admin_frame = AdminFrame(self, self.hospital_queue)
        self.login_frame = LoginFrame(self)
        self.display_frame = DisplayFrame(self, self.hospital_queue)
        
        self.frame_manager.add_frame("display", self.display_frame)
        self.frame_manager.add_frame("login", self.login_frame)
        self.frame_manager.add_frame("admin", self.admin_frame)

        self.frame_manager.switch_to("display")