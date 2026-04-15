Breadth-First Search (BFS) Algorithm
Algorithm: BFS(G, s)

(G = Graph, s = starting vertex)

Create an empty queue Q
Mark all vertices as not visited
Mark the starting vertex s as visited
Insert s into queue Q
While Q is not empty, do:
Remove (dequeue) a vertex u from Q
Visit/print u
For each adjacent vertex v of u:
If v is not visited:
Mark v as visited
Insert v into Q
