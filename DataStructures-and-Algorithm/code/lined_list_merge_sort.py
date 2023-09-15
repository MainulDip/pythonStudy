from linked_list import LinkedList

def merge_sort(linked_list):
    """
    Sorts a linked list in ascending order
    - Recursively divide the linked list into sublist confining a single node
    - Repeatedly merge the sublist to produce sorted sublist until one remains

    Returns a sorted linked list
    """


    if linked_list.size() == 1:
        return linked_list
    elif linked_list.head is None: # if linked_list.size() == 0
        return linked_list
    
    left_half, right_half = split(linked_list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left, right)

def split(linked_list):
    """
    Divide the unsorted list at midpoint into sublist
    """

    # after spiting recursively linked_list on left or right can be empty
    if linked_list == None or linked_list.head == None:
        left_half = linked_list
        right_half = None

        return left_half, right_half
    else:
        size = linked_list.size()
        mid = size // 2

        mid_node = linked_list.node_at_index(mid-1)

        left_half = linked_list
        right_half = LinkedList() # will assign as head for fist node of right half
        right_half.head = mid_node.next_node
        mid_node.next_node = None # making the mid_node as tail node

        return left_half, right_half
    

def merge(left, right): 
    """
    Merges two linked lists, sorting by data in nodes
    Returns a new, merged list
    """

    # Create a new linked list that contains nodes from
    # merging left and right
    merged = LinkedList()

    # Add a fake head that is discarded later
    merged.add(0)

    # Set current to the head of the linked list
    current = merged.head

    # Obtain head nodes for left and right linked list
    left_head = left.head
    right_head = right.head