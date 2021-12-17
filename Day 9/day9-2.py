#https://adventofcode.com/2021/day/9#part2
matrix=[]
with open("testinput.txt", 'r') as file:
    for line in file:
        row = []
        line = line.strip()
        for i in range(0, len(line)):
            row.append([int(line[i]), 0])
        matrix.append(row)


for i in range(0, len(matrix)):
    for j in range(0, len(matrix[i])):
        if j == 0:
            if matrix[i][j][0] < matrix[i][j+1][0]:
                matrix[i][j][1] = 1
        elif j > 0 and j < len(matrix[i]) - 1:
            if matrix[i][j][0] < matrix[i][j+1][0] and matrix[i][j][0] < matrix[i][j-1][0]:
                 matrix[i][j][1] = 1
        else:
            if matrix[i][j][0] < matrix[i][j-1][0]:
                matrix[i][j][1] = 1

for i in range(0, len(matrix)):
    for j in range(0, len(matrix[i])):
        if i == 0:
            if matrix[i][j] < matrix[i+1][j] and matrix[i][j][1] == 1:
                matrix[i][j][1] = 2
        elif i > 0 and i < len(matrix) - 1:
            if matrix[i][j] < matrix[i+1][j] and matrix[i][j] < matrix[i-1][j] and matrix[i][j][1] == 1:
                matrix[i][j][1] = 2
        else:
            if matrix[i][j] < matrix[i-1][j] and matrix[i][j][1] == 1:
                matrix[i][j][1] = 2


for i in range(0, len(matrix)):
    print (matrix[i])


risklevel = 0
for i in range(0, len(matrix)):
    for j in range(0, len(matrix[i])):
        if matrix[i][j][1] == 2:
            risklevel = risklevel + 1 + matrix[i][j][0]
print (risklevel)

