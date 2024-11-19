

# A queue is a First in First out data structure that uses enqueue and dequeue as a way to push and pop items from the list. In python you can import queues from the collections library or just use a list and pop from the front of it and let the default append push items to the back of the list. In C you would use a linked list with structs pointing to each other



class QueueList:
    def __init__(self):
        self.queue = []
    
    def enqueue(self, item):
        self.queue.append(item)  # Add to the end of the list
    
    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)  # Remove from the front of the list
        else:
            raise IndexError("Dequeue from an empty queue")
    
    def is_empty(self):
        return len(self.queue) == 0
    
    def size(self):
        return len(self.queue)

# Example usage:
q1 = QueueList()
q1.enqueue(1)
q1.enqueue(2)
q1.enqueue(3)
print(q1.dequeue())  # Output: 1



from collections import deque

class QueueDeque:
    def __init__(self):
        self.queue = deque()
    
    def enqueue(self, item):
        self.queue.append(item)  # Add to the end
    
    def dequeue(self):
        if not self.is_empty():
            return self.queue.popleft()  # Remove from the front
        else:
            raise IndexError("Dequeue from an empty queue")
    
    def is_empty(self):
        return len(self.queue) == 0
    
    def size(self):
        return len(self.queue)

# Example usage:
q2 = QueueDeque()
q2.enqueue(1)
q2.enqueue(2)
q2.enqueue(3)
print(q2.dequeue())  # Output: 1

