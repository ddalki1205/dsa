class Patient:
    '''
    params:
    - name: str = name of the patient
    - severity: int = starting with 1 indicating low severity, e.g, low priority
    - arrival_time: int = global counter starting with 0 from hospital queue
    '''
    def __init__(self, name: str, severity: int, arrival_time: int):
        self.name: str = name
        self.severity: int = severity
        self.arrival_time: int = arrival_time

    def patient_priority(self) -> tuple:
        '''
        Returns the priority of the patient as a tuple.
        
        Priority is determined by:
        - Negative severity (higher severity is higher priority)
        - Arrival time (earlier arrivals are higher priority for the same severity)
        '''
        return (-self.severity, self.arrival_time)

    def __str__(self):
        return f"{self.name} (Severity: {self.severity}, Arrival: {self.arrival_time})"