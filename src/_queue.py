#!/usr/bin/python3
class HospitalQueue:
    def __init__(self):
        self.queue = []
        self.max = 10

    def enqueue(self, patient, priority):
        if not self.isFull():
            patient_dict = {
                "number": patient,
                "priority": priority
            }

            if patient_dict["priority"] == 1:
                last_priority_patient = -1
                for index in range(self.size()):
                    if self.queue[index]["priority"] == 1:
                        last_priority_patient = index

                if last_priority_patient != -1:
                    self.queue.insert(last_priority_patient + 1, patient_dict)
                else:
                    self.queue.insert(0, patient_dict)
            else:
                self.queue.append(patient_dict)
            return patient_dict
        else:
            return "Error: The queue is full!"

    def dequeue(self):
        if not self.isEmpty():
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
            return self.queue[0]["number"]
        else:
            return "Error the queue is empty!"

    def rear(self):
        if not self.isEmpty():
            return self.queue[-1]["number"]
        else:
            return "Error the queue is empty!"
        
    def printQueue(self):
        return self.queue

    def isFull(self):
        return len(self.queue) == self.max

    def isEmpty(self):
        return len(self.queue) == 0

if __name__ == "__main__":
    queue = HospitalQueue()
    queue.enqueue(1, 0)
    queue.enqueue(4, 1)
    queue.enqueue(5, 1)
    queue.enqueue(6, 1)
    #=queue.dequeue()
    print(f"The element at the front of the queue is {queue.front()}")
    print(f"Queue: {queue.printQueue()}")
