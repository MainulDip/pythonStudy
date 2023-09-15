class Node:
    """
    An Object for storing a single node for a singly linked list.
    Models two attributes: data and the link to the next node in the list
    """

    data = None
    next_node = None

    def __init__(self, data) -> None:
        self.data = data

    def __repr__(self) -> str:
        return "<Node data: %s>" % self.data


# N1 = Node(10)
# N2 = Node(20)
# N3 = Node(30)
# N4 = Node(40)
# N1.next_node = N2
# N2.next_node = N3
# N3.next_node = N4
# print(N1)
# print(N2)

class LinkedList:
    """
    Singly Linked List
    For Singly Linked List, we only need to define head if we are prepending
    If we need to insert items at the last, then we have to define the Tail
    
    """

    def __init__(self) -> None:
        self.head = None # head is linked list's local prop

    def is_empty(self):
        return self.head == None
    
    def size(self):
        # returns the number of nodes in the list, Takes linear O(n) time
        current = self.head
        count = 0

        while current:
            count += 1
            current = current.next_node # digging into all the Node until next_node is None
        
        return count
    
    def add(self, data):
        # adds a new node containing data at head of the list
        # Takes O(1) time
        # on first call, next_node is None (as Head's initial value is None on that point)
        # on first call, we will define the head to the newly inserted Node (after defining next_node)
        # on second call next_node is the first_call's head (which is a Node object)
        # on second call head is the new Node item
        new_node = Node(data)
        new_node.next_node = self.head # assign previously inserted Node object as next_node of the newly created Node
        self.head = new_node # updating class prop head with the newly created Node Object
        # print("self.head : %s" % self.head)

    def search(self, key):
        """
        Search for the first node containing data that matches the key
        Returns the node or `None` if not found
        Takes O(n) || Linear Time
        """
        current = self.head

        while current:
            if current.data == key:
                return current
            else:
                current = current.next_node
        return None
    
    def insert(self, data, index):
        """
        Inserts a new Node contining data at index position
        Insertion takes O(1) time but finding the node at the insertion point take O(n) time
        So takes overall O(n) time
        """
        if index == 0:
            self.add(data)
        
        if index > 0:
            new_node = Node(data)
            position = index
            current = self.head

            while position > 1:
                current = new_node.next_node
                position -= 1

            prev_node = current
            next_node = current.next_node

            prev_node.next_node = new_node
            new_node.next_node = next_node

    def remove(self, key):
        """
        Removes Node Containing data that matches the key
        Returns the node or None if key doesn't exist
        Takes O(n) time
        """
        current = self.head
        previous = None
        found = False

        while current and not found:
            if current.data == key and current is self.head:
                found = True
                self.head = current.next_node
            elif current.data == key:
                found = True
                previous.next_node = current.next_node
            else:
                previous = current
                current = current.next_node
        return current

    def __repr__(self) -> str:
        """
        Showing a string representation of the list
        Takes O(n) times
        """
        nodes = []
        current = self.head

        while current:
            if current is self.head:
                nodes.append("[Head: %s]" % current.data)
            elif current.next_node is None:
                nodes.append("[Tail: %s]" % current.data)
            else:
                nodes.append("[%s]" % current.data)

            current = current.next_node
        
        return '-> '.join(nodes)
    
    # helper suction for merge-sorting linked list
    # setting a index based accesses option
    def node_at_index(self, index):
        if index == 0:
            return self.head
        else:
            current = self.head
            position = 0

            while position < index:
                current = current.next_node
                position += 1

            return current
    
l = LinkedList()
l.add(1)
l.add(2)
l.add(3)
n = l.search(3)
print(n)
# l.head = N1
# print(l.size())
# print("l.head.data: ", l.head.data)
print("l.next_node: ", l.head.next_node)
# print(l)