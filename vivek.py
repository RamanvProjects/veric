ascii_file = open("basic.txt","r")
rows = ascii_file.read().split("\n")
#print rows
graph = {}
x = 0
y = 0
for rx,rv in enumerate(rows):
    for cy,cv in enumerate(rv):
        if cv == " ":
            graph[(rx,cy)] = []
            if graph[(rx-1,cy)] != "wall":
                graph[(rx-1,cy)].append((rx,cy))
                graph[(rx,cy)].append((rx-1,cy))
            if graph[(rx,cy-1)] != "wall":
                graph[(rx,cy-1)].append((rx,cy))
                graph[(rx,cy)].append((rx,cy-1))
        else:
            graph[(rx,cy)] = "wall" 
        y += 1
    x+=1
    y=0

#print graph.keys()
#print graph[(1,1)]
#print graph[(6,1)]

clean_graph = {}
for loc in graph.keys():
    if graph[loc] != "wall":
        clean_graph[loc] = graph[loc]

print clean_graph
