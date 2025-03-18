"""
- A reasonable question is whether BSTs are faster than arrays for value search
- In this exercise, we will explore this question

1. Implement a binary search tree with insertion and search operations as
    seen in class, and binary search in arrays as seen in class [0.2 pts]

2. Measure BST performance using timeit as follows: [0.3 pts]
    1. Generate a 10000-element sorted vector, shuffle, and use it to build a tree by
        inserting each element
    2. Search each element. Time the search (averaged across 10 tries for each element),
        and return average and total time

3. Using the same shuffled vector from question 2: [0.3 pts]
    1. Sort the vector
    2. Search each element using binary search. Time the search (averaged across 10
        tries for each element), and return average and total time

4. Discuss: which approach is faster? Why do you think is that? [0.2 pts]
"""
import random
import timeit


class Node: # (part 1)
    def __init__(self, data, parent=None, left=None, right=None):
        self.parent = parent
        self.data = data
        self.left = left
        self.right = right

def insert(data, root=None): # (part 1)
    current = root
    parent = None

    while current is not None:
        parent = current
        if data <= current.data:
            current = current.left
        else:
            current = current.right

    newnode = Node(data, parent)    
    if root is None:
        root = newnode
    elif data <= parent.data:
        parent.left = newnode
    else:
        parent.right = newnode

    return newnode

def search(data, root): # (part 1)
    current = root
    while current is not None:
        if data == current.data:
            return current
        elif data <= current.data:
            current = current.left
        else:
            current = current.right
    return None

def binarySearch(arr, low, high, x):

    while low <= high:

        mid = low + (high - low) // 2

        if arr[mid] == x:
            return mid

        elif arr[mid] < x:
            low = mid + 1

        else:
            high = mid - 1

    return -1


# (part 2)

root = None
vector1 = list(range(10000)) 

random.shuffle(vector1)

for value in vector1:
    if root is None:
        root = insert(value)
    else:
        insert(value, root)


# (part 2)

total_time_for_trials = 0
trials = 10

for value in vector1:
    time1 = timeit.timeit(lambda: search(value, root), number=trials)
    avg_time_each_element = time1 / trials
    total_time_for_trials += avg_time_each_element

overall_avg_time = total_time_for_trials / len(vector1)

print("\nBalanced BST:\n")

print(f"Overall average search time: {overall_avg_time} seconds")

print(f"Total search time for all elements: {total_time_for_trials} seconds")

# (part 3)


total_time_for_trials = 0
vector1.sort()

for value in vector1:
    time1 = timeit.timeit(lambda: binarySearch(vector1, 0, len(vector1)-1, value), number=trials)
    avg_time_each_element = time1 / trials
    total_time_for_trials += avg_time_each_element

overall_avg_time = total_time_for_trials / len(vector1)

print("\nSorted Array:\n")
print(f"Overall average search time: {overall_avg_time} seconds")

print(f"Total search time for all elements: {total_time_for_trials} seconds")


"""
Question 4:

It appears that the BST approach is slightly faster even though they have the same complexity. 
The time complexity for binary search on a sorted array is theoretically O(logn) which would be the same
as the BST; however, based on certain arithmetic and comparison operations in my binary search implementation, there is a bit more overhead added.
"""