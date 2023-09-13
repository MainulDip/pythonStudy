### Recursive Function:
It's a function that calls itself directly or indirectly inside it's body. 
### How Recursive Function Works:
The base return prevents it from being a infinite recursion (like infinite loop).

The first return call is stored at the bottom of the stack memory (main call) and the base return logic is stored at the top of the stack. All other calls are staked in between. 

Computation in recursion happens from top of the stacks. The top's return is carried over to the next underneath call and one-by-one all the return flows (caring the returned result) to the bottom.

Bottom (main) return is the final return (happens at the last).And main return is halted until all the sub returns are finished, as the main return depends on all the sub returns synchronously.

### Factorial Number:
The factorial of a number is the multiplication of all the numbers between 1 and the number itself. It is written like this: n!. So the factorial of 2 is 2! (= 1 × 2).
n! = n(n-1)!
4! = 4 * 3 * 2 * 1 = 24
Division : 4!/3! = (4 * 3!) / 3! = 4
```python
# Program to print factorial of a number
# recursively.

# Recursive function
def recursive_factorial(n):
if n == 1:
	return n
else:
	return n * recursive_factorial(n-1)

# user input
num = 6

# check if the input is valid or not
if num < 0:
print("Invalid input ! Please enter a positive number.")
elif num == 0:
print("Factorial of number 0 is 1")
else:
print("Factorial of number", num, "=", recursive_factorial(num))
```
### Factorial Use Case (statistics and probabilities):
It is used to solve/get the number of possible arrangements of a given value.

For example, let's see all the arrangements we can have with the three items, A, B and C : ABC, ACB, BAC, BCA, CAB, CBA = 3! = 6
### Tail Optimization (Recursion):
When (in recursive function) call itself as the last call of the function, it will considered as tail call, all other calls other than the last return will be considered head call. Some compiler provide pre-build features to handle tail recursion to be memory optimized.

In this case tail optimization only works on supported language compilers (like JS, Java, Swift, etc).

* To make a recursive function tail optimized, usually the recursive function is wrapped inside another function (wrapper function) and any king of arithmetic operation will be passed as argument/s of the recursive tail call. Python doesn't support tail optimization.