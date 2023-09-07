class Node:
    """
    An Object for storing a single node of a linked list.
    Models two attributes: data and the link to the next node in the list
    """

    data = None
    next_node = None

    def __init__(self, data) -> None:
        self.data = data

    def __repr__(self) -> str:
        return "<Node data: %s>" % self.data


N1 = Node(10)
N2 = Node(20)
N1.next_node = N2

class LinkedList:
    """
    Singly Linked List
    """

    def __init__(self) -> None:
        self.head = None

    def is_empty(self):
        return self.head == None
    
    def size(self):
        # returns the number of nodes in the list, Takes linear O(n) time
        current = self.head
        count = 0

        while current:
            count += 1
            current = current.next_node
        
        return count
    
    def add(self, data):
        # adds a new node containing data at head of the list
        # Takes O(1) time
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node
    
# L = LinkedList()
# L.head = N1
# print(L.size())