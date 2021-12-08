spawns = '3,4,3,1,2'
singleSpawns  = spawns.split(',')
spawnCage = []

for singleSpawn in singleSpawns :
    spawnCage.append([[int(singleSpawn), 0]])

spawnCage1 = spawnCage
iterationCounter = 0


for i in range(0,256):
    for j in range(0, len(spawnCage)):
        spawn = spawnCage[j]
        for h in range(0, len(spawn)):
            if spawn[h][0] > 0:
                spawn[h][0] = spawn[h][0] - 1
            else:
                spawn[h][0] = 6
                spawn[h][1] = spawn[h][1] + 1
                spawn.append([8,0])




