#! /usr/bin/python
#Stack implementation

class Stack:
    
    def __init__(self):
        self.items = []
        self.top = 0
        
    def isEmpty(self):
        return self.items == []
    
    def push(self, item):
        self.items.append(item)
        self.top += 1
        
    def pop(self):
        if len(self.items) <= 0:
            return ("Stack Empty!")
        item = self.items.pop(self.top - 1)
        self.top -= 1
        return item
    
    def size(self):
        return len(self.items)
    
    