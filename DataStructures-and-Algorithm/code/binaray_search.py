def binary_search(list, target):
    first = 0
    last = len(list) - 1

    print("Initial first = %s and last = %s" %(first, last))

    while first <= last:
        midpoint = (first+last) // 2 
        # // is floor division operator which return whole number from a division
        
        if list[midpoint] == target: 
            return midpoint # Best Case
        elif list[midpoint] < target:
            # change the value of first to the first of the right-hand list, the midpoint value will be recalculated
            first = midpoint + 1  
            print("changing first value and now first = %s and last = %s" %(first, last))
        else:
            # change the value of last to the last of the left-hand list, the midpoint value will be recalculated
            last = midpoint -1
            print("changing last value and now first = %s and last = %s" %(first, last))
        
    return None

def verify(index):
    if index is not None:
        print("Target Found at index: ", index)
    else:
        print("Target Not Found")

numbers = [1,2,3,4,5,6,7,8,9,10]

result = binary_search(numbers, 12)
verify(result)

result = binary_search(numbers, 7)
verify(result)