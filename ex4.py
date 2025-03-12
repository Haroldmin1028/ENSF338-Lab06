import numpy as np

class Heap:
    def heapify(self):
        pass
    def enqueue(self, element):
        
        self.heapify()
    def dequeue(self, element):
        
        self.heapify()

def test(heap):
    

def main():
    sorted_array = [x for x in range(10)]
    empty_array = []
    random_array = [np.random.randint(10) for x in range(1000)]
    sorted_heap, empty_heap, random_heap = Heap(), Heap(), Heap()


if __name__ == "__main__":
    main()
