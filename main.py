#! /usr/bin/python
import LinkedList
from BinaryTree import *

def main():
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

if __name__ == "__main__":
    main()