#https://adventofcode.com/2021/day/2
horizontal = 0
vertical = 0
with open("directions.txt", 'r') as file:
    for line in file:
        lineSplit = line.split(' ')
        if lineSplit[0] == 'up':
            vertical = vertical - int(lineSplit[1])
        elif lineSplit[0] == 'down':
            vertical = vertical + int(lineSplit[1])
        else:
            horizontal = horizontal + int(lineSplit[1])
print(horizontal * vertical)




