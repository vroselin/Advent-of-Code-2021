#https://adventofcode.com/2021/day/10#part2
openings = ['(','[','{','<']
closings = [')',']','}','>']
values = [1,2,3,4]
finalValue = 0
missingClosings = []
correctClosings = []
finalResults = []

with open("input.txt", 'r') as file:
    for line in file:
            expected = []
            line = line.strip()
            breakable = 0
            for i in range(0, len(line)):
                if line[i] in openings:
                    expected.append(closings[openings.index(line[i])])
                elif line[i] in closings:
                   if line[i] == expected[-1]:
                        expected.pop(-1)
                   else:
                       breakable = 1
                if breakable == 1:
                    break
            if breakable == 0:
                #print(line)
                missingClosings.append(line)


for line in missingClosings:
    expected = []
    line = line.strip()
    for i in range(0, len(line)):
        if line[i] in openings:
            expected.append(closings[openings.index(line[i])])
        elif line[i] in closings:
            if line[i] == expected[-1]:
                expected.pop(-1)
    correctClosings.append(expected)


finalResult = 0
for expectedClosing in correctClosings:
    temporaryResult = 0
    expectedClosing.reverse()
    for i in range(0, len(expectedClosing)):
        value = values[closings.index(expectedClosing[i])]
        temporaryResult = temporaryResult * 5 + value
    finalResults.append(temporaryResult)

finalResults.sort()
#print(finalResults)

j = (len(finalResults) + 1)/2
#print (j)

print(finalResults[int(j) - 1])




