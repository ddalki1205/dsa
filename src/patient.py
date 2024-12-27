class Patient:
    '''
    params:
    - name: str = name of the patient
    - severity: int = starting with 1 indicating low severity, e.g, low priority
    - arrival_time: str = datetime object of when the patient arrives
    - patient_id: int = a unique ID for the patient (starting from 100)
    '''

    _id_counter = 100  # Class-level counter to generate unique patient IDs

    def __init__(self, name: str, severity: int, arrival_time: object):
        self.name: str = name
        self.severity: int = severity
        self.arrival_time: int = arrival_time
        self.patient_id: int = Patient._id_counter  # Assign the next available ID
        Patient._id_counter += 1  # Increment the counter for the next patient

    def __lt__(self, other):
        """Define the less-than comparison for sorting by severity (lower severity first)."""
        if isinstance(other, Patient):
            return self.severity < other.severity
        return NotImplemented

    def get_line_number(self) -> int:
        '''
        Returns the line number as an integer.

        Line number represents the position that the patient is at in the queue
        '''
        return self.line_number

    def get_priority(self) -> tuple:
        ''' 
        Returns the priority of the patient as a tuple.
        
        Priority is determined by:
        - Negative severity (higher severity is higher priority)
        - Arrival time (earlier arrivals are higher priority for the same severity)
        '''
        return (-self.severity, self.arrival_time)

    def __str__(self):
        return f"{self.name} (Severity: {self.severity}, Arrival: {self.arrival_time}) ID: {self.patient_id})"