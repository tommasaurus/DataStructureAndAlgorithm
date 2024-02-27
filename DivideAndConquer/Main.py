# CS3100 - Spring 2024 - Programming Assignment 2
#################################
# Collaboration Policy: You may discuss the problem and the overall
# strategy with up to 4 other students, but you MUST list those people
# in your submission under collaborators.  You may NOT share code,
# look at others' code, or help others debug their code.  Please read
# the syllabus carefully around coding.  Do not seek published or online
# solutions for any assignments. If you use any published or online resources
# (which may not include solutions) when completing this assignment, be sure to
# cite them. Do not submit a solution that you are unable to explain orally to a
# member of the course staff.
#################################

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
