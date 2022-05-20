# iteration over a sequence ( list, tuple, dictionary, set or string)

people = ['john', 'paul', 'sara', 'susan', 'jorge', 'livoy']

for person in people:
    if person == 'paul':
        continue # stop printing paul but continue the next loop
    if person == 'jorge':
        break # will not print jorge and break/stop whole loop 
    print(f'Current Person: {person}')

# Result
# Current Person: john
# Current Person: sara
# Current Person: susan

# looping using another range
for i in range(len(people)):
    print(people[i])

for i in range(0, 11):
    print(f'Number: {i}')

# While loop
count = 0
while count <= 10:
    print(f'Count: {count}')
    count += 1 # count++ will not work