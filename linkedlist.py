#Personal implementation of the linked list data structure

#Python 3.7.9

#A linked list is a data structure where elements are connected linearly. Each element contains a reference to the next element in line.

class Node:

    # Node class definition. A linked list is made up of Nodes, which include the value it holds and a reference to the next element in the list

    def __init__(self, value):

        self.value = value
        self.next = None

class LinkedList:

    # Linked list definition. Head refers to the first Node in the list. If the head is empty, then the list is empty.

    def __init__(self):

        self.head = None

    # Prints each value in the linked list

    def print(self):

        node = self.head

        while node:

            print(node.value)

            node = node.next

def create_linkedlist():

    # creates a linked list with 3 elements

    linkedlist =LinkedList()

    first = Node(1)

    second = Node(2)

    third = Node(3)

    linkedlist.head = first

    first.next = second

    second.next = third

    return linkedlist

if __name__ == '__main__':

    linkedlist = create_linkedlist()

    linkedlist.print()