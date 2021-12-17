import sys
nodes = {}
with open("testinput1.txt", 'r') as file:
    for line in file:
            line = line.strip()
            line_splitted = line.split('-')
            line_splitted[0].strip()
            line_splitted[1].strip()
            if line_splitted[0] in nodes:
                 nodes[line_splitted[0]].append(line_splitted[1])
            else:
                nodes[line_splitted[0]] = [line_splitted[1]]


print(nodes)




def find_paths(graph, start, end, paths, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    for node in graph[start]:
        print (node)
        if graph.get(node) is not None:
            paths.append(node)
            find_paths(graph, node, end, path)
    return paths




paths = []
allPaths = find_paths(nodes, 'start', 'end', paths)
print(allPaths)