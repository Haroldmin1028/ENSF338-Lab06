import sys
sys.setrecursionlimit(20000)

class Node:
    def __init__(self, data, parent=None, left=None, right=None):
        self.parent = parent
        self.data = data
        self.left = left
        self.right = right

class ExpressionTree:
    def __init__(self, expression):
        self.tokens = expression.split()
        self.index = 0
        self.root = self.parse_expression()
    
    def parse_expression(self):
        if self.index >= len(self.tokens):
            return None
        
        token = self.tokens[self.index]
        self.index += 1
        
        if token == '(':
            left = self.parse_expression()  
            operator = self.tokens[self.index]
            self.index += 1
            right = self.parse_expression()  
            self.index += 1  
            node = Node(operator)
            node.left = left
            node.right = right
            return node
        else:
            return Node(int(token))

    
    def evaluate(self, node=None):
        if node is None:
            node = self.root
            
        if node.left is None and node.right is None:
            return node.data  
        
        left_data = self.evaluate(node.left)
        right_data = self.evaluate(node.right)
        
        if node.data == '+':
            return left_data + right_data
        elif node.data == '-':
            return left_data - right_data
        elif node.data == '*':
            return left_data * right_data
        elif node.data == '/':
            return left_data / right_data
        
    
if __name__ == "__main__":
    expression = "( " + sys.argv[1] + " )"
    tree = ExpressionTree(expression)
    result = tree.evaluate()
    print(result)
