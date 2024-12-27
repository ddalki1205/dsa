# Hospital Queue System

## Project Proposal
> This project aims to address common challenges in hospitals, such as long waiting times and inefficient patient tracking, by implementing a dynamic priority-based queue system. The system ensures that patients with critical conditions are attended to first, improving hospital efficiency and patient care.

## Key Components

### Data Structures and Algorithms

#### 1. Priority Queue
- **Purpose**: Manage patients based on the severity of their condition.
- **Advantages**: Ensures critical patients are prioritized regardless of arrival time, maintaining fairness.

#### 2. Linked Lists
- **Purpose**: Handle the dynamic nature of the queue for efficient insertion and deletion of patients.
- **Advantages**: Provides flexibility in managing patient order based on changing priorities.

#### 3. Heap Implementation
- **Purpose**: Efficiently implement the priority queue for large numbers of patients.
- **Advantages**: Supports fast insertion, deletion, and reordering, ensuring the highest-priority patient is always at the top.

## Expected Functionality

### 1. Patient Registration
- Allow hospital staff to add patients to the queue.
- Input includes:
  - Patient name
  - Severity level
  - Arrival time

### 2. Dynamic Queue Management
- Automatically sort patients by priority:
  - Higher-severity cases are placed at the front of the queue.
  - The queue updates dynamically when:
    - A new patient is added.
    - A patient is attended to and removed.
    - A patient’s severity level is updated.

### 3. Priority Handling
- Patients with higher severity are prioritized over those with lower severity.
- For patients with the same severity, arrival time determines their position (first-come, first-served).

### 4. Queue Display
- Display the current list of patients in priority order.
- Show details such as:
  - Patient name
  - Severity level
  - Position in the queue

### 5. Patient Attendance
- Allow staff to mark the highest-priority patient as "attended," removing them from the queue.
- Automatically reorder the queue after each attendance.

### 6. Error Handling
- Prevent invalid inputs, such as:
  - Missing information
  - Incorrect severity levels
- Notify staff of errors or when attempting to process an empty queue.

## Prerequisites
- [Python](https://www.python.org/downloads/) (version 3.13 above)

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/ddalki1205/hospital-queue-system
    ```

2. Navigate to the project directory:
    ```bash
    cd hospital-queue-system
    ```
3. Install dependencies:
    ```bash
    pip install -r requirements.txt