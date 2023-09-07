# recursive : calling the function itself form it's body
# call the function recursively but with modified parameter input
# if any "return" statement is missing, it will fail to report back to the first caller 
# so every return statement in recursion will make chain and report back to original
# the problem with recursive (with non-recursive) function is it lack the ability to return the target's index position

def binary_search_recursive(list, target):
    if len(list) == 0:
        return False
    else:
        midpoint = (len(list)) // 2

        if list[midpoint] == target:
            return True
        else:
            if list[midpoint] < target:
                return binary_search_recursive(list[midpoint + 1:], target)
                # list[index:] will build new array with the previously supplied list but will start form the index and carry on to the last by denoting ":"
                # if "return" statement is missing, it will fail to report back to the first caller, aka break the chain
            else:
                return binary_search_recursive(list[:midpoint], target)
                # list[:midpoint] is the list[from_beginning...midpoint]
                # if "return" statement is missing, it will fail to report back to the first caller, aka break the chain
            

def verify(result):
    print("Target found: ", result)

numbers = [1,2,3,4,5,6,7,8,9,10]

result = binary_search_recursive(numbers, 12) # if any "return" statement is missing, it will fail to report back to the first caller 
verify(result)

result = binary_search_recursive(numbers, 7)
verify(result)
