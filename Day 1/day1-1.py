counterBigger = 0
counterAll = 0
with open("numbers.txt", 'r') as file:
    for line in file:
        if counterAll > 0:
            if number < int(line):
                counterBigger = counterBigger + 1
        number = int(line)
        counterAll = counterAll + 1
print (counterBigger)