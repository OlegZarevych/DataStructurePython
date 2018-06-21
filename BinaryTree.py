#! /usr/bin/python
#BinaryTree implementation

class BinaryTree:
    
    count = 0
    
    def __init__(self, value):
        self.Left = None
        self.Right = None
        self.key = self.count
        self.data = value
        
    def insert(self, value):
        self.count = self.count + 1
        if  self.data > value:
            if self.Left == None:
                self.Left = BinaryTree(value)
            else:
                self.Left.insert(value)
        if self.data < value:
            if self.Right == None:
                self.Right = BinaryTree(value)
            else:
                self.Right.insert(value)
        else:
            self.data = value
            
    def search(self, value):
        if self.data > value:
            return self.Left.search(value)
        if self.data < value:
            return self.Right.search(value)
        if self.data == value:
            return self.key
        
    def print_tree(self):
        if self.Left:
            self.Left.print_tree()
        print(self.data)
        if self.Right:
            self.Right.print_tree()    
    