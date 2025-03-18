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
import timeit
import numpy as np


class Node:
    def __init__(self, data, parent=None, left=None, right=None):
        self.parent = parent
        self.data = data
        self.left = left
        self.right = right

def insert(data, root=None):
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

def search(data, root):
    current = root
    while current is not None:
        if data == current.data:
            return current
        elif data <= current.data:
            current = current.left
        else:
            current = current.right
    return None




vector1 = []

for i in range(10000):
    vector1.append(i)

root = None

for value in vector1:
    if root is None:
        root = insert(value)
    else:
        insert(value, root)

# this will be completely unbalanced, each node has only a right child (goes diagonally right forever)

total_time = 0
trials = 10

for value in vector1:
    time1 = timeit.timeit(lambda: search(value, root), number=trials)
    avg_time_each_element = time1 / trials
    total_time_for_trials += avg_time_each_element

overall_avg_time = total_time_for_trials / len(vector1)

print(f"Overall average search time: {overall_avg_time} seconds")

print(f"Total search time for all elements: {total_time_for_trials} seconds")
