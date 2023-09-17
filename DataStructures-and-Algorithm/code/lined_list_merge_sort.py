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
        print("called")
        return linked_list
    
    left_half, right_half = split(linked_list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left, right)

def split(linked_list):
    """
    Divide the unsorted list at midpoint into sublist
    """
    # print(linked_list)

    # after spiting recursively linked_list on left or right can be empty
    if linked_list == None or linked_list.head == None:
        left_half = linked_list
        # left_half = None
        right_half = None
        print("have been called once")
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

    """  
    loop: increment head (pointer) to the next until both left and right's next_node is None
    merge/insert left_head and right_head into the fake LinkedList
    on: else block, left head and right head are compared, smallest number is added as in the fake linked list,
    then move the head to next node of that side.
    on: if and elif left over nodes or single node are inserted into the fake linked list and 
    """
    # Iterate over left and right until we reach the tail node of either
    # we will move head one after another by assigning head to the next node on iteration
    while left_head or right_head:
        # if the head node of the left is None, we're past the tail
        # Add the node from right to merged linked list
        if left_head is None:
            current.next_node = right_head
            # Call next of right to set loop condition to False
            right_head = right_head.next_node # will terminate the while loop as right_node is None
        
        # if the head node of right is None, we're past the tail
        # add the tail node from left to merged linked list
        elif right_head is None:
            current.next_node = left_head
            # Call next of left to set loop condition to False
            left_head = left_head.next_node

        else:
            # Not at either tail Node
            # Obtain node data to perform comparison operations
            left_data = left_head.data
            right_data = right_head.data

            # if data on left is less than right, set current.next_node to left node
            if left_data < right_data:
                current.next_node = left_head
                # Move left head to next node, which is None to break the loop
                left_head = left_head.next_node
            else:
                current.next_node = right_head
                right_head = right_head.next_node # to break the loop, as right_head's next_node is None

        # convert current.next_node as new current and proceed next iteration to attach other node to be attach as current.next_node on the if and elif block
        current = current.next_node

    # Now Discard fake head and set first merged node as head, current is already inside of the merged LinkedList, and return the LinkedList
    head = merged.head.next_node
    merged.head = head
    return merged


l = LinkedList()
l.add(10)
l.add(2)
l.add(44)
l.add(15)
l.add(200)

print(l)
sorted_linked_list = merge_sort(l)
print(sorted_linked_list)

"""
[1*,3] [2*,4] = [1, 3] [2, 4]
[1, 3*] [2*, 4] = [1, 2] [3, 4]
We don't need to compare [3,4] as those are already sorted on first recursion
"""