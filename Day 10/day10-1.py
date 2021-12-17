#https://adventofcode.com/2021/day/10
openings = ['(','[','{','<']
closings = [')',']','}','>']
values = [3,57,1197,25137]
finalValue = 0

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
                    finalValue = finalValue + values[closings.index(line[i])]
                    break

print(finalValue)
