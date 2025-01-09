#!/usr/bin/python3
class HospitalQueue:
    def __init__(self, patient, priority):
        self.priority = priority
        self.patient = patient
        self.queue = []
        self.max = 10
        self.patient_dict = {
            "number": self.patient,
            "priority": self.priority
        }

    def check_priority_patients(self):
        if not self.isEmpty:
            for index in range(0, len(self.queue)):
                last_priority_patient = None
                patient = self.queue[index]
                if patient.priority == 1:
                    last_priority_patient = self.queue[index].number
                else:
                    index += 1

            return True if last_priority_patient else False


    def enqueue(self):
        if not self.isFull:
            self.queue.append(self.patient_dict)
            return self.patient
        else:
            return "Error: The queue is full!"
        
    def dequeue(self):
        if not self.isEmpty:
            #index = 0
            for index in range(0, len(self.queue)):
                patient = self.queue[index]
                if patient.priority == 1:
                    self.queue.pop(index)
                    return patient.number
                else:
                    index += 1

    def size(self):
        return len(self.queue)

    def capacity(self):
        return self.max

    def front(self):
        pass

    def rear(self):
        pass

    def isFull(self):
        return True if len(self.queue) == self.max else False

    def isEmpty(self):
        return True if len(self.queue) == 0 else False
