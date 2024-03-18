import sys
import time
from Balance import Balance

fp = open("example.txt", 'r')
lines = fp.readlines()

# Parse the input
bookshelf = []

for i in range(0, len(lines)):
    line = lines[i].strip()
    bookshelf.append(int(line))
       
# Call method and print the result
startT = time.time()
b = Balance()
output = b.compute(bookshelf)
endT = time.time()
print(output)
print("time: "+ str(endT-startT))
