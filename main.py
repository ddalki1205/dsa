from customtkinter import *
from src.hospital_queue import HospitalQueue
from gui.root import RootWindow

hospital_queue = HospitalQueue()
root_window = RootWindow(hospital_queue)

root_window.root.mainloop()