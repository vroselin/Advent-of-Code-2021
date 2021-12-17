#https://adventofcode.com/2021/day/6#part2
import math
spawns = '3,4,3,1,2'
spawnCage = []
singleSpawns  = spawns.split(',')

for singleSpawn in singleSpawns :
    spawnCage.append([int(singleSpawn), 1])



print(spawnCage)

finalSpawns = 0

days = 18
time = 0
for i in range (0, len(spawns)):
    currentSpawn = 1

    time = (days - i)/6
    growth = 2
    if(time > 0):
        currentSpawn = pow(growth, time)
    finalSpawns = finalSpawns + currentSpawn



print(finalSpawns)

print(8%6)

#x(t) = x0 × (1 + r) ^t

