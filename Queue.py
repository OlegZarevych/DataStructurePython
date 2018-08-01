#! /usr/bin/python
#Queue implementation

class Queue:
	
	def __init__(self):
		self.items = []
		self.count = 0
		
	def isEmpty(self):
		return self.items == []
	
	def push(self, item):
		self.items.append(item)
		self.count += 1
		
	def pop(self):
		if len(self.items) <= 0:
			return ("Queue Empty!")
		item = self.items.pop(0)
		self.count -= 1
		return item
	
	def size(self):
		return self.count