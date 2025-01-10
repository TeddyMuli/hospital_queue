# Hospital Queue

This project implements a hospital queue management system using Python and Tkinter. The system allows users to add patients to a queue, admit patients, and view various details about the queue.

## Features

- Add patients to the queue with a specified priority and age.
- Admit patients from the front of the queue.
- Display the size and capacity of the queue.
- Show the front and rear patients in the queue.
- Check if the queue is full or empty.
- Visual representation of the queue using Tkinter.

## Requirements

- Python 3.x
- Tkinter

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/TeddyMuli/hospital_queue.git
    ```
2. Navigate to the project directory:
    ```sh
    cd hospital_queue
    ```

## Usage

1. Run the application:
    ```sh
    python3 src/main.py
    ```

2. The main window will open, displaying the hospital queue management interface.

## File Descriptions

### src/main.py

This file contains the main application code for the hospital queue management system. It uses Tkinter to create a graphical user interface (GUI) for interacting with the queue.

#### Key Components:

- **HospitalApp Class**: Initializes the main application window and sets up the GUI components.
- **update_queue_display Method**: Updates the display of the queue in the GUI.
- **ask_priority Method**: Prompts the user to select a priority for a new patient.
- **add_patient Method**: Adds a new patient to the queue.
- **dequeue_patient Method**: Admits the patient at the front of the queue.

### src/hospital_queue.py

This file contains the  class, which implements the queue management logic.

#### Key Methods:

- **enqueue**: Adds a patient to the queue based on priority and age.
- **dequeue**: Admits the patient at the front of the queue.
- **size**: Returns the current size of the queue.
- **show_size**: Displays the current size of the queue.
- **capacity**: Returns the maximum capacity of the queue.
- **show_capacity**: Displays the maximum capacity of the queue.
- **front**: Displays the patient at the front of the queue.
- **rear**: Displays the patient at the rear of the queue.
- **printQueue**: Returns the current queue.
- **isFull**: Checks if the queue is full.
- **showFull**: Displays whether the queue is full.
- **isEmpty**: Checks if the queue is empty.
- **showEmpty**: Displays whether the queue is empty.

## Example

To add a patient to the queue, click the "Add Patient" button, enter the patient's age, and select the priority from the dropdown menu. The patient will be added to the queue based on the specified priority and age.

To admit a patient, click the "Admit Patient" button. The patient at the front of the queue will be admitted, and the next patient will be displayed.
