#! /usr/bin/python
#Linked list implementation

class node:
    def __init__(self):
        self.data = None # contains the data
        self.next = None # contains the reference to the next node


class linked_list:
    def __init__(self):
        self.first = None
        self.last = None

    def add_node(self, data):
        new_node = node() # create a new node
        new_node.data = data
        if self.first == None:
            self.first = new_node
            self.last = self.first
        elif self.last == self.first:
            self.last = new_node
            self.first.next = self.last
        else:
            self.last.next = new_node
            self.last = new_node
        
    def list_print(self):
        node = self.first 
        while node:
            print (node.data)
            node = node.next
    
    def add_first(self, data):
        new_node = node() # create a new node
        new_node.data = data
        new_node.next = self.first
        self.first = new_node

    def remove_last(self):
        self.last = None
        #TODO
            