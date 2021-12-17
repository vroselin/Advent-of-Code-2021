#https://adventofcode.com/2021/day/3#part2
oxygenArray = []
scrubberArray = []
with open("binary.txt", 'r') as file:
    for line in file:
        line = line.strip()
        oxygenArray.append(line)
        scrubberArray.append(line)


i = 0

for i in range(0, 12):
    oneCounter = 0
    zeroCounter = 0
    for element in oxygenArray:
        if int(element[i]) == 1:
            oneCounter = oneCounter + 1
        else:
            zeroCounter = zeroCounter + 1

    if zeroCounter > oneCounter:
        oxygenArray = [element for element in oxygenArray if int(element[i]) == 0]
    else:
        oxygenArray = [element for element in oxygenArray if int(element[i]) == 1]

    if len(oxygenArray) == 1:
        break


i = 0
for i in range(0, 12):
    oneCounter = 0
    zeroCounter = 0
    for element in scrubberArray:
        if int(element[i]) == 1:
            oneCounter = oneCounter + 1
        else:
            zeroCounter = zeroCounter + 1
    if oneCounter >= zeroCounter:
        scrubberArray = [element for element in scrubberArray if int(element[i]) == 0]
    else:
        scrubberArray = [element for element in scrubberArray if int(element[i]) == 1]
    if len(scrubberArray) == 1:
        break

print(int(scrubberArray[0], 2) * int(oxygenArray[0], 2))





