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
            bingoNumbers.append(char)
lineCounter = 0

with open("bingoBoards.txt", 'r') as file:
    for line in file:
        if line.strip():
            line_splitted = line.split(' ')
            for char in (line_splitted):
                if char.strip():
                    char = char.strip()
                    bingoBoard.append([char,0])
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

print(correctResults)

resultArray = []
for i in range(0, 5):
    resultArray.append(i * 6)
#correctResults.append(resultArray)

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
                print(bingos)
                break
        if solved == 1:
            break
        boardCounter = boardCounter + 1

    if solved == 1:
        lastNumber = bingoResult
        break


score = 0
winningBoard = bingoBoards[boardCounter]

for field in winningBoard:
    if field[1] == 0:
        score = score + int(field[0])

print('winning board: ' + str(boardCounter))
print('last drawn number: ' + str(lastNumber))
print('Sum of not winning numbers: ' + str(score))
final = int(score) * int(lastNumber)
print('final score: ' + str(final))



print(boardString)

