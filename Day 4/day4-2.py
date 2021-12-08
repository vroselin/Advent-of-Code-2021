#https://adventofcode.com/2021/day/4
from operator import itemgetter
lineCounter = 0
bingoBoard = []
bingoBoards = []
bingoNumbers = []
with open("bingoDrawings.txt", 'r') as file:
    for line in file:
        line = line.strip()
        line_splitted = line.split(',')
        for char in line_splitted:
            bingoNumbers.append(int(char))
lineCounter = 0

with open("bingoBoards.txt", 'r') as file:
    for line in file:
        if line.strip():
            line_splitted = line.split(' ')
            for char in (line_splitted):
                if char.strip():
                    char = char.strip()
                    bingoBoard.append([int(char),0])
        else:
            bingoBoards.append(bingoBoard)
            if len(line.strip()) == 0:
                bingoBoard = []

bingoBoards.append(bingoBoard)

numberCounter = 0
boardString = ''
correctResults = []


resultArray = []
for i in range(0, 5):
    for j in range (0, 5):
        resultArray.append(i + j*5)
    correctResults.append(resultArray)
    resultArray = []


resultArray = []
for i in range (1, 26):
    resultArray.append(i - 1)
    if i % 5 == 0:
        correctResults.append(resultArray)
        resultArray = []

#correctResults.append(resultArray)
print(correctResults)

#diagonalen
resultArray = []
for i in range(0, 5):
    resultArray.append(i * 6)
    if i % 5 == 0:
        correctResults.append(resultArray)

resultArray = []
for i in range(1, 6):
    resultArray.append(i * 4)
#correctResults.append(resultArray)
bingos = []

solverArray = []
#for i range(0, len(bingoBoards)):
    #solverArray[i] = false

solved = 0
numberCounter = 1
boardCounter = 0
lastNumber = 0
solvedBoards = []

for i in range(0, len(bingoBoards)):
    solvedBoards.append(0)

print(solvedBoards)
currentWinner = []
for bingoResult in bingoNumbers:
    boardString = ''
    boardCounter = 0
    for bingoBoard in bingoBoards:
        cellCounter = 1
        for bingoNumber in bingoBoard:
            if bingoNumber[0] == bingoResult:
                bingoNumber[1] = 1
                boardString = boardString + '\033[92m' + str(bingoNumber[0]) + '\033[0m'
            elif bingoNumber[1] == 1:
                boardString = boardString + '\033[92m' + str(bingoNumber[0]) + '\033[0m'
            else:
                boardString = boardString + str(bingoNumber[0])
            if cellCounter%5 == 0:
                boardString = boardString + '\n'
            else:
                boardString = boardString + ' '
            cellCounter = cellCounter + 1
        boardString = boardString + '\n\n'
        for correctResult in correctResults:
            bingos = itemgetter(*correctResult)(bingoBoard)
            solved = 0
            for bingo in bingos:
                solved = 1
                if bingo[1] == 0:
                    solved = 0
                    break
            if solved == 1:
                break
        if solved == 1:
            currentWinner = bingoBoard
            solvedBoards[boardCounter] = 1
        for solvedBoard in solvedBoards:
            if solvedBoard == 0:
                solved = 0
                break
        if solved == 1:
            break
        boardCounter = boardCounter + 1
    lastNumber = bingoResult
    winningBoard = currentWinner
    if solved == 1:
        break

score = 0


for field in winningBoard:
    if field[1] == 0:
        score = score + int(field[0])

print('last drawn number: ' + str(lastNumber))
print('Sum of not winning numbers: ' + str(score))
final = int(score) * int(lastNumber)
print('final score: ' + str(final))
print(boardString)

print(winningBoard)