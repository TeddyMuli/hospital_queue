#!/usr/bin/env python3
"""
Teddy Muli
SCT211-0023/2022
"""
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
            { "name": "Add Patient", "command": self.add_patient },
            { "name": "Admit Patient", "command": self.dequeue_patient },
            { "name": "Size", "command": self.queue.show_size },
            { "name": "Capacity", "command": self.queue.show_capacity },
            { "name": "Front Patient", "command": self.queue.front },
            { "name": "Rear Patient", "command": self.queue.rear },
            { "name": "Full?", "command": self.queue.showFull },
            { "name": "Empty?", "command": self.queue.showEmpty },
        ]

        self.root.title('Hospital Queue')
        self.root.geometry('800x600')

        self.main_container = tk.Frame(root)
        self.main_container.pack(expand=True, fill=tk.BOTH)

        self.button_frame = tk.Frame(self.main_container)
        self.button_frame.pack(side=tk.TOP, pady=10, fill=tk.X)

        for button in self.buttons:
            tk.Button(self.button_frame, text=button['name'], command=button['command']).pack(side=tk.LEFT, padx=5)

        self.canvas = tk.Canvas(self.main_container)
        self.scrollbar = ttk.Scrollbar(self.main_container, orient=tk.HORIZONTAL, command=self.canvas.xview)
        self.queue_frame = tk.Frame(self.canvas)

        self.canvas.configure(xscrollcommand=self.scrollbar.set)
        
        self.scrollbar.pack(side=tk.BOTTOM, fill=tk.X)
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.canvas_frame = self.canvas.create_window((0, 0), window=self.queue_frame, anchor=tk.NW)

        self.hospital_image = tk.PhotoImage(file=hospital_image_path)
        self.person_image = tk.PhotoImage(file=person_image_path)

        self.hospital_label = tk.Label(self.queue_frame, image=self.hospital_image)
        self.hospital_label.pack(side=tk.RIGHT, padx=5)

        self.queue_frame.bind('<Configure>', self.on_frame_configure)
        self.canvas.bind('<Configure>', self.on_canvas_configure)

        self.queue_frame.pack(expand=True, fill=tk.BOTH)

        self.update_queue_display()

    def on_frame_configure(self, event=None):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def on_canvas_configure(self, event):
        self.canvas.itemconfig(self.canvas_frame, width=event.width)

    def update_queue_display(self):
        for widget in self.queue_frame.winfo_children():
            if widget != self.hospital_label:
                widget.destroy()

        for patient in (self.queue.printQueue()):
            patient_frame = tk.Frame(self.queue_frame)
            patient_frame.pack(side=tk.RIGHT, padx=2, pady=(84, 0))

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

        self.on_frame_configure()

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
