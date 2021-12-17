#https://adventofcode.com/2021/day/14#part-2
import re
from functools import reduce


instructions = []
replacements = {}
with open("testinput.txt", 'r') as file:
    for line in file:
            line = line.strip()
            line_splitted = line.split('->')
            line_splitted[0] = line_splitted[0].strip()
            line_splitted[1] = line_splitted[1].strip()
            key = line_splitted[0]
            value = line_splitted[0][0] + line_splitted[1] + line_splitted[0][1]
            replacements[key] = value
            instructions.append([line_splitted[0].strip(),line_splitted[1].strip()])


polymer = 'NNCB'

#polymer = 'VPPHOPVVSFSVFOCOSBKF'
""" replaced = ''.join(idx if idx not in replacements else replacements[idx] for idx in polymer)
print(replaced)
counter = 0 """


counter = 0
while counter < 10:
    replaceIt = dict((re.escape(k), v) for k, v in replacements.items())
    pattern = re.compile("|".join(replacements.keys()))
    polymer = pattern.sub(lambda m: replacements[re.escape(m.group(0))], polymer)
    counter = counter + 1

characterCounter = 0
characterValues = {}

for character in polymer:
    if character in characterValues:
        characterValues[character] = characterValues[character] + 1
    else:
        characterValues[character] = 1

print (polymer)
sorted = sorted(characterValues.values())
result = sorted[-1] - sorted[0]

print(result)

