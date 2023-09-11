def merge_sort(list):
    """
    Sort a list in ascending order
    Returns a new Sorted list
    Has 3 main steps
    : Divide -> Find the midpoint of the list and divide into sublist
    : Conquer -> Recursive sort the sublist created in previous step
    : Combine -> Merge the sorted sublist created in previous steps
    """

    # Base logic of recursive functions
    if len(list) <= 1:
        return list # naively sorted also it will break the recursion and return the single element list back to the recursion chain
    
    left_half, right_half = split(list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    # the final return will be halted until all recursion finished starting from the base.

    return merge(left, right)

def split(list):
    """
    Divide the unsorted list at midpoint into sublist
    Returns two sublist - left and right 
    """

    mid = len(list) // 2
    left = list[:mid] # 0 until mid (will not include the mid itself)
    right = list[mid:] # from mid point to end (will include midpoint)

    return left, right

def merge(left, right):
    """
    Merges 2 lists/arrays, sorting them in the process
    Returns a new merged list
    """

    l = []
    i = 0 # left index
    j = 0 # right index

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            l.append(left[i])
            i += 1
        else:
            l.append(right[j])
            j += 1

    # handle the last array/list element if left has odd number of elements
    while i < len(left):
        l.append(left[i])
        i += 1

    # handle the last array/list if right has odd number of elements
    while j < len(right):
        l.append(right[j])
        j += 1   

    # print(l) 

    return l

list_unsorted = [9,7,6,4]
sorted_list = merge_sort(list_unsorted)
print(sorted_list)

"""
recursion stack structure for merge sorting of [*, *, *, *] 4 digits

[*] vs [*]    [*] vs [*]    ---------------- Base Logic at top of the stack

  [*, *]   vs   [*, *]     ---------------- Wait Until Base Logic/Comparison finished returning

       [*,*,*,*]          ---------------- main caller wait for it's above return and finally returns the main
"""