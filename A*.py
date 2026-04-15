import heapq

def a_star(graph, heuristic, start, goal):
    pq = []
    heapq.heappush(pq, (0, start))

    g_cost = {start: 0}
    parent = {start: None}

    while pq:
        f_cost, node = heapq.heappop(pq)

        # Goal reached
        if node == goal:
            path = []
            while node:
                path.append(node)
                node = parent[node]

            path.reverse()
            print("Path:", path)
            print("Total Cost:", g_cost[goal])
            return

        # Explore neighbors
        for neighbor, weight in graph[node]:
            new_cost = g_cost[node] + weight

            if neighbor not in g_cost or new_cost < g_cost[neighbor]:
                g_cost[neighbor] = new_cost
                f = new_cost + heuristic[neighbor]
                heapq.heappush(pq, (f, neighbor))
                parent[neighbor] = node

    print("No path found")


# Graph
graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('D', 3), ('E', 1)],
    'C': [('F', 5)],
    'D': [],
    'E': [('F', 2)],
    'F': []
}

# Heuristic values
heuristic = {
    'A': 5,
    'B': 3,
    'C': 4,
    'D': 2,
    'E': 1,
    'F': 0
}

# Call function
a_star(graph, heuristic, 'A', 'F')
