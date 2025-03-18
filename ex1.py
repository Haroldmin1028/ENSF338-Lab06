"""
- BST performance depends on whether the tree is balanced or not
- In this exercise we are going to look at randomization as a way to
improve balancing
-----------------------------------------------------------------------------
1. Implement a binary search tree with insertion and search operations as
    seen in class [0.2 pts]
2. Measure search performance using timeit as follows: [0.3 pts]
    1. Generate a 10000-element sorted vector and use it to build a tree by inserting
        each element
    2. Search each element. Time the search (averaged across 10 tries for each element),
        and return average and total time
3. Measure search performance using timeit as follows: [0.3 pts]
    1. Shuffle the vector used for question 2 (using random.shuffle)
    2. Search each element. Time the search (averaged across 10 tries for each element),
        and return average and total time
4. Discuss the results. Which approach is faster? Why? [0.2 pts]
"""
import sys
import timeit
import numpy as np
import random

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



# Vector (part 2)
vector1 = []

for i in range(10000):
    vector1.append(i)

root = None

for value in vector1:
    if root is None:
        root = insert(value)
    else:
        insert(value, root)

# this will be completely unbalanced, each node has only a right child (goes diagonally right forever) (part 2)

total_time_for_trials = 0
trials = 10

for value in vector1:
    time1 = timeit.timeit(lambda: search(value, root), number=trials)
    avg_time_each_element = time1 / trials
    total_time_for_trials += avg_time_each_element

overall_avg_time = total_time_for_trials / len(vector1)

print(f"Overall average search time: {overall_avg_time} seconds")

print(f"Total search time for all elements: {total_time_for_trials} seconds")

# shuffling and re timing using same vector, just randomly shuffled (part 3)


random.shuffle(vector1)
root = None
for value in vector1:
    if root is None:
        root = insert(value)
    else:
        insert(value, root)

    
# these are the outputs for (part 3)
total_time_for_trials = 0 

for value in vector1:
    time1 = timeit.timeit(lambda: search(value, root), number=trials)
    avg_time_each_element = time1 / trials
    total_time_for_trials += avg_time_each_element

overall_avg_time = total_time_for_trials / len(vector1)

print(f"Overall average search time: {overall_avg_time} seconds")

print(f"Total search time for all elements: {total_time_for_trials} seconds")


"""
The approach used in part 3 is much faster than the approach used in part 2. This is due to the approach in part 3 being 
much more balanced than in part 2. In part 2, the tree wasn't balanced; every node had a right child and thus had a structure of a linked list.
The tree for part 2 was at the worst case, meaning it dgenerates into a linked list due to the sorted vector leaving a height of n-1. That is a
time complexity of O(n). For the case in part 3, the vector was randomized, then when re inputted into the tree, the tree was left
well balanced making the searches much more efficient. This gave a time complexity of O(logn)
"""