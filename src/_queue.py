#!/usr/bin/python3
class HospitalQueue:
    def __init__(self):
        self.queue = []
        self.max = 10

    def check_priority_patients(self):
        if not self.isEmpty():
            for index in range(0, len(self.queue)):
                last_priority_patient = None
                patient = self.queue[index]
                if patient["priority"] == 1:
                    last_priority_patient = patient["number"]
            return last_priority_patient is not None
        return False

    def enqueue(self, patient, priority):
        if not self.isFull():
            patient_dict = {
                "number": patient,
                "priority": priority
            }

            if patient_dict["priority"] == 1:
                last_priority_patient = -1
                for index in range(len(self.queue)):
                    if self.queue[index]["priority"] == 1:
                        last_priority_patient = index

                if last_priority_patient != -1:
                    self.queue.insert(index + 1, patient_dict)
                else:
                    self.queue.insert(0, patient_dict)
            else:
                self.queue.append(patient_dict)
            return patient
        else:
            return "Error: The queue is full!"

    def dequeue(self):
        if not self.isEmpty():
            if self.check_priority_patients():
                for index in range(0, len(self.queue)):
                    patient = self.queue[index]
                    if patient["priority"] == 1:
                        self.queue.pop(index)
                        return patient["number"]
            else:
                self.queue.pop(0)
                return self.queue[0]["number"]
        else:
            return "Error: the queue is empty!"

    def size(self):
        return len(self.queue)

    def capacity(self):
        return self.max

    def front(self):
        if not self.isEmpty():
            if self.check_priority_patients():
                for index in range(0, len(self.queue)):
                    patient = self.queue[index]
                    if patient["priority"] == 1:
                        return patient["number"]
            else:
                return self.queue[0]["number"]
        else:
            return "Error the queue is empty!"


    def rear(self):
        if not self.isEmpty():
            if self.check_priority_patients():
                for index in reversed(range(0, len(self.queue))):
                    patient = self.queue[index]
                    if patient["priority"] == 0:
                        return patient["number"]
            else:
                return self.queue[-1]["number"]
        else:
            return "Error the queue is empty!"


    def isFull(self):
        return len(self.queue) == self.max

    def isEmpty(self):
        return len(self.queue) == 0
