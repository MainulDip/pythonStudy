def fibonacci(n):
    """
    Get the nth position fibonacci number
    """
    if n < 2:
        return n
    else:
        return (fibonacci(n-1) + fibonacci(n-2))
    
# print(fibonacci(4)) # 3

def getFibUpTo(number):
    fibArr = []
    iteration = 0
    while iteration <= number:
        fibArr.append(fibonacci(iteration)) # starting from 0
        iteration += 1
    return fibArr

print(getFibUpTo(10))

"""
On recursive function the first return is stored at the bottom of the stack (main)
and base return logic is stored at the top of the stack. All other calls are staked in between. 
Computation in recursion happens from top of the stacks return and flows (caring the return) to the bottom
Bottom (main) return is the final return and are chained with inner returns. And main return is halted until all the sub returns
"""