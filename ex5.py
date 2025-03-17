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

class ListPriorityQueue:
    def __init__(self):
        self.head = None
    def enqueue(self, node):
        if self.head is None or node.getData() < self.head.getData():
            self.head = node
        else:
            current = self.head
            while current.getNext() is not None and current.getNext().getData() <= node.getData():
                current = current.getNext()
            node.setNext(current.getNext())
            current.setNext(node)
        
    def dequeue(self):
        if self.head is None:
            return None
        element = self.head.getData()
        self.head = self.head.getNext()
        return element  


class HeapPriorityQueue:
    def __init__(self, array):
        self.heap = array
        for i in range(len(self.heap) // 2 - 1, -1, -1):
            self.heapify_down(i)
    def heapify_down(self, index):
        min = index
        left = 2 * index + 1
        right = 2 * index + 2
        if left < len(self.heap) and self.heap[left] < self.heap[min]:
            min = left
        if right < len(self.heap) and self.heap[right] < self.heap[min]:
            min = right
        if min != index:
            self.heap[index], self.heap[min] = self.heap[min], self.heap[index]
            self.heapify_down(min)
    def heapify_up(self, index):
        parent = (index - 1) // 2
        if index > 0 and self.heap[index] < self.heap[parent]:
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            self.heapify_up(parent)
    def enqueue(self, element):
        self.heap.append(element)
        self.heapify_up(len(self.heap) - 1)
    def dequeue(self):
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        min = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.heapify_down(0)
        return min

def randomlist():
    return ['enqueue' if np.random.randint(1, 10) > 3 else 'dequeue' for x in range(NUM_TASKS)]

def queue_list(pqueue, tasks):
    for task in tasks:
        if task == 'enqueue':
            pqueue.enqueue(Node(np.random.randint(10000)))
        else:
            pqueue.dequeue()

def queue_heap(pqueue, tasks):
    for task in tasks:
        if task == 'enqueue':
            pqueue.enqueue(np.random.randint(10000))
        else:
            pqueue.dequeue()

def main():
    list_pq = ListPriorityQueue()
    heap_pq = HeapPriorityQueue([])
    list_time, heap_time = 0, 0

    list_time = timeit.timeit(lambda: queue_list(list_pq, randomlist()), number = 1)
    heap_time = timeit.timeit(lambda: queue_heap(heap_pq, randomlist()), number = 1)

    print(f"ListPriorityQueue -- Overall Time: {list_time}s, Average Time Per Task: {list_time / NUM_TASKS}")
    print(f"HeapPriorityQueue -- Overall Time: {heap_time}s, Average Time Per Task: {heap_time / NUM_TASKS}")

if __name__ == "__main__":
    main()

"""
4.  The two implementations take similar time in this code, but usually HeapPriorityQueue would be faster because its insertion and removal are O(log n), whereas for ListPriorityQueue, its enqueue is O(n) and dequeue is O(1). HeapPriorityQueue also has to heapify up or down every enqueuing and dequeuing, so with the small size of task_list, this may have affected the measured times for this exercise.
"""
