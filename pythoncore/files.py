# open a file
myFile = open('myfile.txt', 'w')

# file info
print('Name : ', myFile.name)
print('Is Closed : ', myFile.closed)
print('Opening Mode : ', myFile.mode)

# writing to the file
myFile.write('Learning python')
myFile.write(' and diving deeper into tensorflow :)')
myFile.close()

# Appending
myFile = open('myfile.txt', 'a')
myFile.write('\n also learnig the integration of the AI with mobile and web toolkit')
myFile.close()

# File Reading
myFile = open('myfile.txt', 'r+')
text = myFile.read(177)
print(text)