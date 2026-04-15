#breadth first search
BFS(G, s):
    create queue Q
    mark s as visited
    enqueue s into Q

    while Q is not empty:
        u = dequeue Q
        print u

        for each vertex v in adjacency list of u:
            if v is not visited:
                mark v as visited
                enqueue v into Q
