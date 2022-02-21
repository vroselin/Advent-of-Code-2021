#https://adventofcode.com/2021/day/15
#https://www.geeksforgeeks.org/python-program-for-min-cost-path/
import collections
numbers = []
counter = 0
with open("testinput.txt", 'r') as file:
    for line in file:
        line = line.strip()
        numbers.append([])
        length = len(line)
        for i in range(0, length):
            numbers[counter].append(int(line[i]))
        counter = counter + 1

def minCost(cost, m, n):

    tc = [[0 for x in range(m+1)] for x in range(n+1)]

    tc[0][0] = cost[0][0]

    for i in range(1, m + 1):
        tc[i][0] = tc[i-1][0] + cost[i][0]

    for j in range(1, n + 1):
        tc[0][j] = tc[0][j-1] + cost[0][j]
    visited = []
    visited.append([0,0])
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            moved = 0
            if j > m - 1 and i < m:
                checkArray = [tc[i-1][j], tc[i][j-1], tc[i+1][j]]
                while moved == 0:
                    minIndex = checkArray.index(min(checkArray))
                    if minIndex == 0 and [i-1,j] not in visited:
                        visited.append([i-1,j])
                        tc[i][j] = min(checkArray) + cost[i][j]
                        moved = 1
                    elif minIndex == 1 and [i, j-1] not in visited:
                        visited.append([i, j-1])
                        tc[i][j] = min(checkArray) + cost[i][j]
                        moved = 1
                    elif minIndex == 2 and [i+1,j] not in visited:
                        visited.append([i+1,j])
                        tc[i][j] = min(checkArray) + cost[i][j]
                        moved = 1
                    if moved == 1 or len(checkArray) == 1:
                        print(moved)
                        break
                    checkArray.pop(minIndex)

            elif j < m and i > m - 1:
                checkArray = [tc[i-1][j], tc[i][j-1], tc[i][j+1]]
                while moved == 0:
                    minIndex = checkArray.index(min(checkArray))
                    if minIndex == 0 and [i-1,j] not in visited:
                        visited.append([i-1,j])
                        tc[i][j] = min(checkArray) + cost[i][j]
                        moved = 1
                    elif minIndex == 1  and [i, j-1] not in visited:
                        visited.append([i, j-1])
                        tc[i][j] = min(checkArray) + cost[i][j]
                        moved = 1
                    elif minIndex == 2 and [i,j+1] not in visited:
                        visited.append([i,j+1])
                        moved = 1
                        tc[i][j] = min(checkArray) + cost[i][j]
                    if moved == 1 or len(checkArray) == 1:
                        print(moved)
                        break
                    checkArray.pop(minIndex)
            elif j < m and i < m:
                checkArray = [tc[i-1][j], tc[i][j-1],tc[i+1][j], tc[i][j+1]]
                while moved == 0:
                    minIndex = checkArray.index(min(checkArray))
                    if minIndex == 0 and [i-1,j] not in visited:
                        visited.append([i-1,j])
                        tc[i][j] = min(checkArray) + cost[i][j]
                        moved = 1
                    elif minIndex == 1  and [i, j-1] not in visited:
                        visited.append([i, j-1])
                        tc[i][j] = min(checkArray) + cost[i][j]
                        moved = 1
                    elif minIndex == 2 and [i+1,j] not in visited:
                        visited.append([i+1,j])
                        tc[i][j] = min(checkArray) + cost[i][j]
                        moved = 1
                    elif minIndex == 3 and [i,j+1] not in visited:
                        visited.append([i,j+1])
                        tc[i][j] = min(checkArray) + cost[i][j]
                        moved = 1
                    if moved == 1 or len(checkArray) == 1:
                        print(moved)
                        break
                    checkArray.pop(minIndex)
            else:
                checkArray = [tc[i-1][j], tc[i][j-1]]
                while moved == 0:
                    minIndex = checkArray.index(min(checkArray))
                    if minIndex == 0 and [i-1,j] not in visited:
                        visited.append([i-1,j])
                        tc[i][j] = min(checkArray) + cost[i][j]
                        moved = 1
                    elif minIndex == 1 and [i,j-1] not in visited:
                        visited.append([i, j-1])
                        tc[i][j] = min(checkArray) + cost[i][j]
                        moved = 1
                    if moved == 1 or len(checkArray) == 1:
                        print(moved)
                        break
                    checkArray.pop(minIndex)


    return tc[m][n]



#cost = minCost(numbers, R - 1, C - 1) - numbers[0][0]
#print(cost)
print(minCost(numbers, len(numbers[0]) - 1, len(numbers) - 1) - numbers[0][0])
