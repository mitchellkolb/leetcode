

# A queue is a First in First out data structure that uses enqueue and dequeue as a way to push and pop items from the list. In python you can import queues from the collections library or just use a list and pop from the front of it and let the default append push items to the back of the list. In C you would use a linked list with structs pointing to each other

"""
The Time Complexity of using queues that use python lists and/or collections are
Enqueue O(1), Dequeue O(1), Peeking O(1)
"""


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

"""
# This is a C code version that I wanted to include becuase it uses linked lists that are attached by the next pointers


#include <stdio.h>
#include <stdlib.h>

// Define a node in the queue
typedef struct Node {
    int data;
    struct Node* next;
} Node;

// Define the queue
typedef struct Queue {
    Node* front; // Points to the front of the queue
    Node* rear;  // Points to the rear of the queue
} Queue;

// Function to initialize a new queue
Queue* createQueue() {
    Queue* q = (Queue*)malloc(sizeof(Queue));
    q->front = q->rear = NULL;
    return q;
}

// Function to enqueue an item
void enqueue(Queue* q, int item) {
    Node* newNode = (Node*)malloc(sizeof(Node));
    newNode->data = item;
    newNode->next = NULL;
    if (q->rear == NULL) { // If the queue is empty
        q->front = q->rear = newNode;
        return;
    }
    q->rear->next = newNode;
    q->rear = newNode;
}

// Function to dequeue an item
int dequeue(Queue* q) {
    if (q->front == NULL) { // If the queue is empty
        printf("Queue underflow\n");
        return -1;
    }
    Node* temp = q->front;
    int item = temp->data;
    q->front = q->front->next;
    if (q->front == NULL) {
        q->rear = NULL;
    }
    free(temp);
    return item;
}

// Function to check if the queue is empty
int isEmpty(Queue* q) {
    return q->front == NULL;
}

// Example usage:
int main() {
    Queue* q = createQueue();
    enqueue(q, 10);
    enqueue(q, 20);
    printf("%d\n", dequeue(q)); // Output: 10
    enqueue(q, 30);
    printf("%d\n", dequeue(q)); // Output: 20
    return 0;
}


"""