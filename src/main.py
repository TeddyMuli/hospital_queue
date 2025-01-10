#!/usr/bin/env python3
import tkinter as tk
from tkinter import simpledialog
from hospital_queue import HospitalQueue

person_image_path = "../assets/person.png"
hospital_image_path = "../assets/hospital.png"

class HospitalApp:
    def __init__(self, root):
        self.root = root
        self.queue = HospitalQueue()

        self.root.title('Hospital Queue')
        self.root.geometry('800x600')

        self.hospital_image = tk.PhotoImage(file=hospital_image_path)
        self.person_image = tk.PhotoImage(file=person_image_path)

        self.hospital_label = tk.Label(root, image=self.hospital_image)
        self.hospital_label.pack(side=tk.RIGHT, padx=5)

        self.queue_frame = tk.Frame(root)
        self.queue_frame.pack(side=tk.RIGHT, padx=5, fill=tk.X)

        self.add_patient_button = tk.Button(root, text="Add Patient", command=self.add_patient)
        self.add_patient_button.pack(side=tk.TOP, pady=10)

        self.dequeue_patient_button = tk.Button(root, text="Dequeue Patient", command=self.dequeue_patient)
        self.dequeue_patient_button.pack(side=tk.TOP, pady=10)

        self.update_queue_display()

    def update_queue_display(self):
        for widget in self.queue_frame.winfo_children():
            widget.destroy()

        for patient in reversed(self.queue.printQueue()):
            patient_frame = tk.Frame(self.queue_frame)
            patient_frame.pack(side=tk.LEFT, padx=2)

            info_label = tk.Label(patient_frame, text=f"Number: {patient['number']}\nPriority: {patient['priority']}\nAge: {patient['age']}")
            info_label.pack()

            patient_label = tk.Label(patient_frame, image=self.person_image)
            patient_label.pack()

    def add_patient(self):
        number = simpledialog.askinteger("Input", "Enter patient number:")
        priority = simpledialog.askinteger("Input", "Enter patient priority:")
        age = simpledialog.askinteger("Input", "Enter patient age:")

        if number is not None and priority is not None and age is not None:
            self.queue.enqueue(number, priority, age)
            self.update_queue_display()

    def dequeue_patient(self):
        self.queue.dequeue()
        self.update_queue_display()

if __name__ == "__main__":
    root = tk.Tk()
    app = HospitalApp(root)
    root.mainloop()
