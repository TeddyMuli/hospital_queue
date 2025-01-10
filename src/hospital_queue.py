#!/usr/bin/python3
class HospitalQueue:
    def __init__(self):
        self.queue = []
        self.max = 10

    def enqueue(self, patient, priority, age):
        if not self.isFull():
            patient_dict = {
                "number": patient,
                "priority": priority,
                "age": age
            }

            if not self.isEmpty():
                insert_at = -1
                for index in range(self.size()):
                    if patient_dict['priority'] > self.queue[index]['priority']:
                        insert_at = index
                        break
                    elif patient_dict['priority'] == self.queue[index]['priority']:
                        if (self.queue[index]['age'] < 70 or self.queue[index]['age'] < 5) and (patient_dict['age'] > 70 or patient_dict['age'] < 5):
                            insert_at = index
                        else:
                            insert_at = index + 1
                        break

                self.queue.insert(insert_at, patient_dict)
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
            return "Error: the queue is empty!"

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
    queue.enqueue(1, 0, 23)
    queue.enqueue(2, 1, 16)
    queue.enqueue(3, 3, 43)
    queue.enqueue(4, 0, 71)
    queue.enqueue(5, 2, 2)
    queue.enqueue(6, 6, 45)
    print(f"Queue: {queue.printQueue()}")
