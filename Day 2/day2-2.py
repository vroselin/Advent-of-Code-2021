#https://adventofcode.com/2021/day/2#part2
horizontal = 0
vertical = 0
aim = 0
with open("directions.txt", 'r') as file:
    for line in file:
        lineSplit = line.split(' ')
        if lineSplit[0] == 'up':
            aim =  aim - int(lineSplit[1])
        elif lineSplit[0] == 'down':
            aim =  aim + int(lineSplit[1])
        else:
            horizontal = horizontal + int(lineSplit[1])
            vertical = vertical + int(lineSplit[1]) * aim
print(vertical * horizontal)




