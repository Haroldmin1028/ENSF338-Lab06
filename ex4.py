import numpy as np

class Heap:
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
    return ['enqueue' if np.random.randint(1, 10) > 3 else 'dequeue' for x in range(100)]

def isHeap(array, index, end):
    if index >= int((end - 1) / 2):
        return True
    if (array[index] <= array[2 * index + 1] and array[index] <= array[2 * index + 2] and isHeap(array, 2 * index + 1, end) and isHeap(array, 2 * index + 2, end)):
        return True
    return False

def test(array):
    actual_heap = Heap(array)

    for task in randomlist():
        if task == 'enqueue':
            item = np.random.randint(1000)
            actual_heap.enqueue(item)
        else:
            actual_heap.dequeue()
        if not isHeap(actual_heap.heap, 0, len(actual_heap.heap) - 1):
            print("Error! Did not pass test")
            return
    print("Success! Passed test")

def main():
    temp = [x for x in range(1000)]
    np.random.shuffle(temp)
    test_list = [[x for x in range(10)], [], temp]
    for array in test_list:
        test(array)


if __name__ == "__main__":
    main()
