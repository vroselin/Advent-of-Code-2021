#https://adventofcode.com/2021/day/5
largestNumberX = 0
largestNumberY = 0
coordinatesList = []
with open("input.txt", 'r') as file:
    for line in file:
            line = line.strip()
            line_splitted = line.split('->')
            coordinatesList.append([line_splitted[0].strip(), line_splitted[1].strip()])
            for numbers in line_splitted:
                number = numbers.split(',')
                if int(number[0]) > int(largestNumberX):
                    largestNumberX = int(number[0])
                if int(number[1]) > int(largestNumberY):
                    largestNumberY = int(number[1])



diagram = []

rangeX = largestNumberX+1
rangeY = largestNumberY+1

for i in range(0,rangeY+1):
    diagram.append([])
    for j in range (0,rangeX+1):
        diagram[i].append(0)

""" for line in diagram:
    print(line) """
#print(diagram[0][0])
#print(coordinatesList)
counter = 0
for coordinates in coordinatesList:
    startingPoint = coordinates[0].split(',')
    endPoint = coordinates[1].split(',')
    if int(startingPoint[0]) < int(endPoint[0]):
        startX = int(startingPoint[0])
        endX = int(endPoint[0])
    else:
        startX = int(endPoint[0])
        endX = int(startingPoint[0])

    if int(startingPoint[1]) < int(endPoint[1]):
        startY = int(startingPoint[1])
        endY = int(endPoint[1])
    else:
        startY = int(endPoint[1])
        endY = int(startingPoint[1])


    if startX == endX:
        for i in range (startY, endY + 1 ):
            diagram[startX][i] = diagram[startX][i] + 1
    if startY == endY:
        for i in range(startX, endX + 1):
            diagram[i][startY] = diagram[i][startY] + 1


overlapcounter = 0
for line in diagram:
    for i in range(0,len(line)):
        if line[i] > 1:
            overlapcounter = overlapcounter + 1


print(overlapcounter)
