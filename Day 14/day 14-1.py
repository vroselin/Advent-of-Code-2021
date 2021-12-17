#https://adventofcode.com/2021/day/14
instructions = {}
with open("testinput.txt", 'r') as file:
    for line in file:
            line = line.strip()
            line_splitted = line.split('->')
            instructions[line_splitted[0].strip()] = line_splitted[1].strip()

counter = 0
polymer = 'NNCB'
#polymer = 'VPPHOPVVSFSVFOCOSBKF'
newInstruction = ''
while counter < 10:
    for i in range(0, len(polymer) - 1):
        if i == 0:
            newInstruction = polymer[i] + instructions[polymer[i]+polymer[i+1]] + polymer[i+1]
        else:
            newInstruction = newInstruction + instructions[polymer[i]+polymer[i+1]] + polymer[i+1]


    counter = counter + 1
    polymer = newInstruction
    newInstruction = ''

characterCounter = 0
characterValues = {}

for character in polymer:
    if character in characterValues:
        characterValues[character] = characterValues[character] + 1
    else:
        characterValues[character] = 1


sorted = sorted(characterValues.values())
result = sorted[-1] - sorted[0]

print(result)
