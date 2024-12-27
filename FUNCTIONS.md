# DO NOT INTERACT WITH PATIENT CLASS DIRECTLY
- hospital queue will act as the service layer

## Functionality of hospital queue
public functions for the hospital queue available to be used

> [!IMPORTANT]
> Severity is based on a scale of 1-10
> 1 being the lowest severity and priority

- **add_patient(name, severity)**:
    - where name is a string and severity is an int between 1-10
- **remove_patient(self)**:
    - removes the patient in the front of the queue and returns them
- **update_severity(name, new_severity)**:
    - where name is the patient's name in the program and the new_severity is the new integer between 1-10
- **find_patient(name)**:
    - searches for the patient in the queue and returns them(as an object) or none if not found
- **display_queue()**:
    - ONLY FOR THE TERMINAL
    - displays the queue based on priority