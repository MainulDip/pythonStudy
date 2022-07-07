## Python Core Quick Docs

### Sequence Vs Collection
Lists, tuples, and strings are sequences. 
Things come out of them in the same order they were put in.

Sets and dictionaries are collections. 
The ordering of items in sets is arbitrary.
(It's not random, and it's technically not unpredictable, but it's good to think of it as both.) 
The ordering of keys and values in dictionaries is also arbitrary.

Physically, collections have an order - every time you iterate over a set you'll visit its items in the same order - but the order may change if you add or remove items