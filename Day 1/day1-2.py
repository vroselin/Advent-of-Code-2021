#https://adventofcode.com/2021/day/1
counterBigger = 0
counterAll = 0
numbers = []
with open("numbers.txt", 'r') as file:
    for line in file:
        numbers.append(int(line))
        counterAll = counterAll + 1
    print(counterAll)
    for x in range(1, counterAll - 1):
        if x > 1:
            oldSum = sum
        sum = int(numbers[x-1]) + int(numbers[x]) +int(numbers[x+1])
        if x > 1:
            if sum > oldSum:
                counterBigger = counterBigger + 1
        x = x + 1

print(counterBigger)


