### Overview:
DataStructure and Algorithm in Pythons

### Algorithm:
Generally Its a set of steps or instruction for completing a task, like a recipe, etc. 

In CS, A set of (optimized) steps a program takes to finish a tasks or solve a problem. Or we can say, some better approaches (practices) to solve computation problems.

### Algorithm Guidelines:
* Algorithm clearly defines problem statement, input and output
* steps need to be in a very specific order
* steps need to distinct (consistent )
* should produce a result
* should complete in a finite amount of time

### Algorithmic Thinking:
These are some approach to solve computation problem by 
- breaking down the problem into several pieces, each with clearly defined input and output 
- along with some distinct set of steps that solve all those problem through input ot output
- and grouping with suitable Algorithm.

NB: it does not come overnight, its practice.

### Big O || O(n):
Its the theoretical definition of the complexity of an algorithm as a function of the size. It's a notation used to describe complexity.
O(n): Order of magnitude of complexity. n is "A function of the size". O(n) measures complexity as the input size grows (on the worst case scenario/n/Upper Bounds).

### Efficiency of Algorithm:
- Efficiency (Time): Time Complexity (how long does it take to complete a task). or Runtime Complexity.

- Efficiently (Space): Space Complexity (how much memory it consume to complete a task)

### Runtime Per Operation || Constant Time || O(1):
Reading a value in a list takes same amount of time for every case. it is described in O(1) notation (where 1 is a constant) and reads "constant time" (big O of 1).

### Efficiency Measurement:
- Best Case Scenario (first value in linear search and middle value in binary search)
- Worst Time Scenario (n): last value in both linear and binary search. It's the most important to measure algorithm efficiency.
- Order Of Growth: in terms of worst case scenario as n, how much more steps is required when n grows compared to other algorithm when comparing.
### Notes on Following Math:
* Logarithm: It's the inverse of taking the exponent(pow) of something. It takes 2 input, base and power value. and the output is the power (pow)
 - log (base 2) of 8 = 3 || 2^3 = 8

### Search Algorithms and worst (n) case runtime || Polynomial Runtime:
Worst case runtime means: the highest time of tries it can take to find a number. Worst case number is denoted by "n"
---- Linear Runtime:
* Linear/Sequential/Simple Search: Searching something form start position of a list/array and proceed with next until get the match.
 -> sort is not required
 -> O(n)

 ---- Logarithmic/SubLinear Runtime: when runtime is base on logarithm

* Binary Search: search a number in a sorted list by splitting it in half and comparing the number with the last (highest) number of each list and proceed with the selected list group and carry on until found
 - also known as half-interval search, logarithmic search, or binary chop,
 - true (1) or false (0), either this or that. 
 - list needs to be sorted.
 - O(log n) or O(ln n) or (Log2 of n) + 1
 - ex: for finding the last number (as n) of a 0 to 16 range list (sorted list), it will take log2 of 16 + 1 tries, which is 4 + 1 = 5

* Merge Sort (unsorted to sorted list) : its a recursive algorithm that continuously splits the array in half until it cannot be further divided, then it start comparing left with right to sort and continuously build the sorted final array/list 
 - O(n log n)

---- Polynomial Runtime: an algorithm will considered Polynomial Runtime if it's worst case runtime is "n raised by K power" or O(n^K)
* Quadratic Runtime:
 - O(n^2)
* Cubic Runtime:
 - O(n^3)
* Quasi Linear Runtime:
 - O(n log n)
 - it falls between linear and Quadratic Runtime (in Graph)
 - like Merge Sort Algorithm

 ### Exponential Runtime || O(x ^ n)|| Non Efficient Runtime:
 * Brute Force Runtime: to find a password between 00 to 99 brute force tries will end-up with 10^2
 * Factorial/Combinatorial Runtime O(n!): n!: n(n-1)(n-2)...(2)(1)
  - like Traveler Map for shortest distance
  - 3! = 3*2*1 = 6
  - factorial of 4 = 4! = 4*3*2*1 = 24
### Recursion and its Depth:
* Recursive Function: the function that call itself form its body and implement some breaking condition inside it
* Recursive Depth: the number of time a recursive function call itself until finished, is called Recursive Depth
### Iterative vs Recursive:
* Iterative solution is something that is loop based. its opposite of recursion.
* python favours iterative approach, hence it has Recursive Depth Limit
* languages those favour recursive function will not have any recursion depth limit

### Functional Languages:
CS text books back in the days favour functional language coding.
- in functional language programmer avoid to change function's local variable (make those immutable). Functional language prefer recursion over iterative solution.

### Recursive vs Iterative and Space Complexity:
- Iterative functions usually have a constant space complexity. consume same amount of space in memory/ram while running and until finished

### Recursion and Tail Optimization or Tail Optimized Language:
- recursive function needs to allocate additional new memory (half of previous call, n->n/2->n/4...) on each recursion, hence it consume more memory if the programming language does not deal with this. 
- python is not a tail optimized language like swift. hence it consumes more memory (logarithmic memory || O(log n)) while on recursive implementation.
* Head vs Tail Recursion: If a function call itself at the beaning of its body, then it is the head recursion. If called at the end, its tail recursion.
* Tail Call Optimization/Elimination: Language like swift implement these to prevent the increasing ram allocation on recursive function. aka minimize O(log n) space complexity for recursion.
### Now: 1.49.47