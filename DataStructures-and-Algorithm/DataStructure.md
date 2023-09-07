### DataStructure Prerequisite:
Linked with
- Big O notation | O(n)
- Time and Space Complexity
- Recursion
- Divide and Conquer
### What is Data Structure:
- it's a data storage format. 
- it is the collection of values and the format they are stored in
- the relationships between the values in the collection as well as the operation applied on the data stored in the structure.

### Operations on Data Structure:
- access and read values
- search for arbitrary values
- insert values at any point into structure
- delete values in the structure

### Data Structure Types:
- Contiguous Data Structure: stored side by side in memory/ram. Strictly typed languages store data this way as all array elements are same data types
- Non Contiguous: Stored different palaces and are linked with pointers (*). Dynamic languages (python, etc) store array pointer in contiguous manner but store the pointed value different places in the memory.

### Array/list:
- homogeneous array container: store same type of data in array, like java/swift
- heterogeneous array container : can store different types data, like python/php (non typed languages )
- in CS, array and list are different, list are actually linked-list
- storage allocation: when arrays are initialize, the contiguous block is allocated by "Space = N * M" || n = index, m = first element of the array
- inserting new element at the starting (index 0) position of an existing array add time complexity, it adds up with shifting operation to rest of the elements. But appending (insert at the last position) does not add time complexity.

### Linked List: 
- arrays are good at accessing (which happens in constant time O(1)) but bad at inserting/deleting (linear time O(n)) elements other than last index.
- linked lists are better for insertion/deletion than accessing/reading. for lots of insertion/deletion operation linked-lists are better option than array.
* its a linear data structure where each elements of it is a self contained object called "Node". Nodes are call self referential objects
- Node store 2 information, the individual stored data and link/reference to the next element.
* every linked list has head and tail. Tail Node has no link
* linked list holds a reference of the head (sometimes tail also)
* can be
- Singly Linked List : carries only after/next link/pointer 
- Doubly Linked List : carries both before/previous and after/next link/pointers
