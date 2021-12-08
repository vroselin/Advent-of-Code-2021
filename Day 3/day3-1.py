#https://adventofcode.com/2021/day/3
lines = []
values = []
linesCounter = 0
charactersCounter = 0

with open("binary.txt", 'r') as file:
    for line in file:
        line = line.strip()
        charactersCounter = 0
        for char in line:
            char = int(char)
            if linesCounter == 0:
                values.append(char)
            else:
                values[charactersCounter] = char + values[charactersCounter]
            charactersCounter = charactersCounter + 1
        linesCounter = linesCounter + 1


gammaValue = 0
epsilonValue = 0
counter = len(values) - 1
for character in values:
    if character < linesCounter / 2:
        gamma = 0
        epsilon = 1
    else:
        gamma = 1
        epsilon = 0
    gammaValue = gammaValue + (2**counter) * gamma
    epsilonValue = epsilonValue + (2**counter) * epsilon
    counter = counter - 1

print(gammaValue * epsilonValue)