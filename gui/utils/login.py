import os

class HospitalKiosk:
    MAX_ATTEMPTS = 4

    def __init__(self):
        self.admin_credentials = {"username": "admin", "password": "admin123"}
        self.patient_credentials = {"username": "patient", "password": "patient123"}

    def login(self):
        attempts = HospitalKiosk.MAX_ATTEMPTS

        while attempts > 0:
            username = input("Enter your username: ")
            password = input("Enter your password: ")

            if self.validate_credentials(username, password):
                return username
            attempts -= 1
            if attempts > 0:
                print(f"\nInvalid credentials. You have {attempts} attempts left.")
            else:
                print("\nToo many failed attempts. Please try again later.")
        return None

    def validate_credentials(self, username, password):
        if username == self.admin_credentials["username"] and password == self.admin_credentials["password"]:
            return "admin"
        elif username == self.patient_credentials["username"] and password == self.patient_credentials["password"]:
            return "patient"
        return None

    def run(self):
        user = self.login()
        if user == "admin":
            print("\nLogged in as Admin.")
        elif user == "patient":
            print("\nLogged in as Patient.")
        else:
            print("\nLogin failed. Exiting.")
