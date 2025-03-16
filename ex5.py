import timeit, numpy as np

NUM_TASKS = 1000

class Node:
    def __init__(self, value):
        self._value = value
        self._next = None
    def getData(self):
        return self._value
    def setData(self, value):
        self._value = value
    def getNext(self):
        return self._next
    def setNext(self, next):
        self._next = next

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def enqueue(self, node):
        if self.head is not None:
            node.setNext(self.head)
        elif self.head is None:
            self.tail = node
        self.head = node
    def dequeue(self):
        if self.head is None:
            return None
        elif self.head == self.tail:
            element = self.tail.getData()
            self.head = self.tail = None
            return element
        else:
            current = self.head
            while current.getNext() != self.tail:
                current = current.getNext()
            element = self.tail.getData()
            self.tail = current
            self.tail.setNext(None)
            return element    

class ListPriorityQueue(LinkedList):
    pass

class Heap:
    pass

#does not need additional priority queue implementation
class HeapPriorityQueue(Heap):
    pass

def randomlist():
    return ['enqueue' if np.random.randint(1, 10) > 3 else 'dequeue' for x in range(NUM_TASKS)]

def queue(pqueue, tasks):
    for task in tasks:
        if task == 'enqueue':
            pqueue.enqueue(Node(np.random.randint(10000)))
        else:
            pqueue.dequeue()

def main():
    list_pq = ListPriorityQueue()
    heap_pq = HeapPriorityQueue(1000)
    list_time, heap_time = 0, 0

    list_time = timeit.timeit(lambda: queue(list_pq, randomlist()), number = 1)
    heap_time = timeit.timeit(lambda: queue(heap_pq, randomlist()), number = 1)

    print(f"ListPriorityQueue -- Overall Time: {list_time}s, Average Time Per Task: {list_time / NUM_TASKS}")
    print(f"HeapPriorityQueue -- Overall Time: {heap_time}s, Average Time Per Task: {heap_time / NUM_TASKS}")


if __name__ == "__main__":
    main()

"""
4.  
"""
