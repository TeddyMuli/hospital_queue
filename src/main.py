#!/usr/bin/env python3
import tkinter as tk
from hospital_queue import HospitalQueue

image_path = "../assets/person.png"

if __name__ == "__main__":
    root = tk.Tk()
    root.title('Hospital Queue')
    root.geometry('600x500')

    image = tk.PhotoImage(file=image_path)
    label = tk.Label(root, image=image)
    label.pack()
    root.mainloop()
