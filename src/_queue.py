#!/usr/bin/python3
class HospitalQueue:
    def __init__(self, patient, priority):
        self.priority = priority
        self.patient = patient
        self.queue = []
        self.max = 10

    def enqueue(self):
        if not self.isFull:
            pass

    def dequeue(self):
        if not self.isEmpty:
            pass

    def size(self):
        return len(self.queue)

    def capacity(self):
        pass

    def front(self):
        pass

    def rear(self):
        pass

    def isFull(self):
        return True if len(self.queue) == self.max else False

    def isEmpty(self):
        return True if len(self.queue) == 0 else False
