paper = []
for i in range(0,15):
    paper.append([])
    for j in range(0,15):
        paper[i].append('.')



with open("testinput.txt", 'r') as file:
    for line in file:
            line = line.strip()
            line_splitted = line.split(',')
            paper[int(line_splitted[0])][int(line_splitted[1])] = '#'

""" for i in range(0, len(paper)):
    print(paper[i]) """


c = 1
for i in range (0,14):
    for j in range (0,14):
        if paper[i][j] == '#' or paper[i+c][j] == '#':
            paper[i][j] = '#'
            c = c + 1


for i in range(0,8):
    paper.pop()

dotCounter = 0
for i in range(0, len(paper)):
    #print(paper[i])
     for j in range (0,14):
        if paper[i][j] == '#':
            dotCounter = dotCounter + 1

print(dotCounter)



