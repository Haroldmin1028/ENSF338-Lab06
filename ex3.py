import sys

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
        
def calculate(expression_array):
    return 0

def search(expression):
    expression = expression.replace('(', ' ( ').replace(')', ' ) ')
    expression_array = expression.split()

    return calculate(expression_array)


def main():
    root = Node(100)
    expression = sys.argv[1]
    result = search(expression)
    print(result)


if __name__ == "__main__":
    main()