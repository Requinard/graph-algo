import graph
import random

g = graph.Graph()

rand = random.Random()

for i in range(1, 100):
    v = g.add_vertex(i)

    if i >= 10:
        for j in range(0, 3):
            v1 = g.vertexes[rand.randint(0, i - 1)]

            g.add_edge(v, v1)


print "BFS"
e = g.breadth_first_search(5)

print "DFS"
e = g.depth_first_search(5)