def merge_sort(list):
    """
    Sort a list in ascending order
    Returns a new Sorted list
    Has 3 main steps
    : Divide -> Find the midpoint of the list and divide into sublist
    : Conquer -> Recursive sort the sublist created in previous step
    : Combine -> Merge the sorted sublist created in previous steps
    """

    # counter = 0
    # counter += 1

    if len(list) <= 1:
        return list # naively sorted also it will break the recursion and return the single element list back to the recursion chain
    
    left_half, right_half = split(list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    # this will be called when all recursion is finished
    
    # print(counter, " : ", left," and ", right)

    print("list:", list, left, right, "lengths", len(left), len(right))
    
    # if len(left) == 2 and len(right) == 2:

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
    # counter = 0
    # counter += 1
    # print(counter, " : ", left," and ", right)

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

alist = [9,7,6,4, -4, 3]
result = merge_sort(alist)
# print(alist)
print(result)
