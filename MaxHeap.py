#! /usr/bin/python
#Max heap implementation

import math

class max_heap:
    
    def __init__(self):
        self.heap = []
        self.count = 0
        
    
    def push(self, data):
        if self.count == 0:
            self.heap.insert(self.count, data)
            self.count += 1
        
        else:
            self.count += 1
            self.heap.insert(self.count, data)
            self.__sort(len(self.heap) - 1)
            #self.sort()
    
    #another implementation
    def sort(self):
        current = self.count - 1
        parent = math.floor(current / 2)     
        while current > 0 and self.heap[parent] < self.heap[current]:
            self.heap[current], self.heap[parent] = self.heap[parent], self.heap[current]
            current = parent
            parent = math.floor(current / 2)     
        
            
    def __sort(self, current):
        parent = math.floor(current / 2)     
        if self.heap[parent] < self.heap[current]:
            self.heap[current], self.heap[parent] = self.heap[parent], self.heap[current]
            if parent <= 0:
                return
            else:
                self.__sort(parent)
                    
    def pop(self):
        pass
    
    def remove(self):
        pass
    
    def length(self):
        return self.count
    
    def is_empty(self):
        return self.count == 0;
    
    def print(self):
        print(self.heap)