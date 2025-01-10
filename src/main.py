#!/usr/bin/env python3
import tkinter as tk
from tkinter import simpledialog, ttk
from hospital_queue import HospitalQueue

person_image_path = "../assets/person.png"
hospital_image_path = "../assets/hospital.png"

class HospitalApp:
    def __init__(self, root):
        self.root = root
        self.queue = HospitalQueue()

        self.buttons = [
            { "name": "Add Patient", "command": self.queue.enqueue },
            { "name": "Admit Patient", "command": self.queue.dequeue },
            { "name": "Size", "command": self.queue.show_size },
            { "name": "Capacity", "command": self.queue.show_capacity },
            { "name": "Front Patient", "command": self.queue.front },
            { "name": "Rear Patient", "command": self.queue.rear },
            { "name": "Full", "command": self.queue.showFull },
            { "name": "Empty", "command": self.queue.showEmpty },
        ]

        self.root.title('Hospital Queue')
        self.root.geometry('800x600')

        self.hospital_image = tk.PhotoImage(file=hospital_image_path)
        self.person_image = tk.PhotoImage(file=person_image_path)

        self.hospital_label = tk.Label(root, image=self.hospital_image)
        self.hospital_label.pack(side=tk.RIGHT, padx=5)

        self.queue_frame = tk.Frame(root)
        self.queue_frame.pack(side=tk.RIGHT, padx=5, fill=tk.X)

        self.button_frame = tk.Frame(root)
        self.button_frame.pack(side=tk.TOP, pady=10)

        for button in self.buttons:
            self.add_patient_button = tk.Button(self.button_frame, text=button['name'], command=button['command'])
            self.add_patient_button.pack(side=tk.LEFT, padx=5)

        self.update_queue_display()

    def update_queue_display(self):
        for widget in self.queue_frame.winfo_children():
            widget.destroy()

        for patient in reversed(self.queue.printQueue()):
            patient_frame = tk.Frame(self.queue_frame)
            patient_frame.pack(side=tk.LEFT, padx=2, pady=(84, 0))

            match patient['priority']:
                case 0:
                    priority = "Normal"
                case 1:
                    priority = "Serious"
                case 2:
                    priority = "Critical"

            info_label = tk.Label(patient_frame, text=f"Number: {patient['number']}\nPriority: {priority}\nAge: {patient['age']}")
            info_label.pack()

            patient_label = tk.Label(patient_frame, image=self.person_image)
            patient_label.pack()

    def ask_priority(self):
        priority_window = tk.Toplevel(self.root)
        priority_window.title("Select Priority")
        
        window_width = 300
        window_height = 150
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        position_top = int(screen_height / 2 - window_height / 2)
        position_right = int(screen_width / 2 - window_width / 2)
        priority_window.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")

        tk.Label(priority_window, text="Select patient priority:").pack(pady=10)

        priority_var = tk.StringVar()
        priority_combobox = ttk.Combobox(priority_window, textvariable=priority_var)
        priority_combobox['values'] = ('normal', 'serious', 'critical')
        priority_combobox.pack(pady=10)
        priority_combobox.current(0)

        def on_select():
            self.selected_priority = priority_combobox.current()
            priority_window.destroy()

        select_button = tk.Button(priority_window, text="OK", command=on_select)
        select_button.pack(pady=10)

        def on_close():
            self.selected_priority = None
            priority_window.destroy()

        priority_window.protocol("WM_DELETE_WINDOW", on_close)

        self.root.wait_window(priority_window)
        return self.selected_priority

    def add_patient(self):
        number = self.queue.size() + 1
        age = simpledialog.askinteger("Input", "Enter patient age:")

        if age is not None:
            priority = self.ask_priority()
            if priority is not None:
                self.queue.enqueue(number, priority, age)
                self.update_queue_display()

    def dequeue_patient(self):
        self.queue.dequeue()
        self.update_queue_display()

if __name__ == "__main__":
    root = tk.Tk()
    app = HospitalApp(root)
    root.mainloop()
