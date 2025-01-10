#!/usr/bin/env python3
from tkinter import messagebox

class HospitalQueue:
    def __init__(self):
        self.queue = []
        self.max = 7

    def enqueue(self, patient, priority, age):
        if not self.isFull():
            patient_dict = {
                "number": patient,
                "priority": priority,
                "age": age
            }

            if not self.isEmpty():
                for index in range(self.size()):
                    if patient_dict['priority'] > self.queue[index]['priority']:
                        insert_at = index
                        break
                    elif patient_dict['priority'] == self.queue[index]['priority']:
                        if (self.queue[index]['age'] < 60 and self.queue[index]['age'] > 5) and (patient_dict['age'] > 60 or patient_dict['age'] < 5):
                            insert_at = index
                            break
                        else:
                            insert_at = index + 1
                    else:
                        insert_at = self.size()

                self.queue.insert(insert_at, patient_dict)
            else:
                self.queue.append(patient_dict)

        else:
            messagebox.showwarning("Warning" ,"The queue is full!")

    def dequeue(self):
        if not self.isEmpty():
            messagebox.showinfo("Info", f"Admitted patient: {self.queue[0]['number']}\nNext Patient: {self.queue[1]['number'] if self.size() > 1 else 'None'}")
            self.queue.pop(0)
        else:
            messagebox.showwarning("Warning", "The queue is empty!")

    def size(self):
        return len(self.queue)
    
    def show_size(self):
        messagebox.showinfo("Size", f'The size of the queue: {self.size()}')

    def capacity(self):
        return self.max
    
    def show_capacity(self):
        messagebox.showinfo("Capacity", f'The capacity of the queue: {self.capacity()}')

    def front(self):
        if not self.isEmpty():
            messagebox.showinfo("Front", f'The front patient is {self.queue[0]["number"]}')
        else:
            messagebox.showwarning("Warning", "The queue is empty!")

    def rear(self):
        if not self.isEmpty():
            messagebox.showinfo("Rear", f'The front patient is {self.queue[-1]["number"]}')
        else:
            messagebox.showwarning("Warning", "The queue is empty!")

    def printQueue(self):
        return self.queue

    def isFull(self):
        return len(self.queue) == self.max
    
    def showFull(self):
        messagebox.showinfo("Full", f'The queue is {"full" if self.isFull() else "not full"}')

    
    def isEmpty(self):
        return len(self.queue) == 0
    
    def showEmpty(self):
        messagebox.showinfo("Empty", f'The queue is {"empty" if self.isEmpty() else "not empty"}')

if __name__ == "__main__":
    queue = HospitalQueue()
    queue.enqueue(1, 1, 23)
    queue.enqueue(2, 1, 89)
    queue.enqueue(3, 2, 34)
    queue.enqueue(4, 0, 12)
    queue.enqueue(5, 2, 2)
    queue.enqueue(6, 6, 45)
    print(f"Queue: {queue.printQueue()}")
