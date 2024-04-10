# CS3100 - Spring 2024 - Programming Assignment 4
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
import re
from roller_coaster import RollerCoaster

fp = open("terrain.txt", 'r')
lines = fp.readlines()
terrain = []
for line in lines:
    terrain.append([int(i) for i in re.findall(r'\d+', line.strip())])


start = time.time()
rc = RollerCoaster()
length = rc.compute(terrain)
print("length:    " + str(length))
print("terrains:  " + str(rc.getCoasterPath()))
print("start pos: " + str(rc.getCoasterStart()))
end = time.time()
print("time:      "+ str(end-start))

