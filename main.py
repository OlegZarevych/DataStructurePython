#! /usr/bin/python
import LinkedList
from BinaryTree import *
from Stack import *

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

if __name__ == "__main__":
    main()