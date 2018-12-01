#! /usr/bin/python
import LinkedList
from BinaryTree import *
from Stack import *
from Queue import *
from MaxHeap import max_heap

def main():
    
    print("Linked list implementation")
    ll = LinkedList.linked_list()
    ll.add_node(1)
    ll.add_node(2)
    ll.add_node(3)
    ll.list_print()
     
    print("Binary tree implementation")
    tree = BinaryTree(1)
    tree.insert(2)
    tree.insert(5)
    tree.insert(8)
    tree.insert(3)
    tree.print_tree()
    print(tree.search(8))
 
    print("Stack implementation")
    stack = Stack()
    print(stack.size)
    stack.push("first")
    print(stack.size)
    stack.push("second")
    print(stack.size)
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    print(stack.size())
     
    print("Queue implementation")
    q = Queue()
    q.push("first")
    q.push("second")
    print(q.pop())
    print(q.pop())
    
    print("Heap implementation")
    h = max_heap()
    h.push(10)
    h.push(3)
    h.push(9)
    h.push(7)
    h.push(14)
    h.push(8)
    h.push(16)
    h.push(2)
    h.push(1)
    h.push(4)
    h.print()

if __name__ == "__main__":
    main()