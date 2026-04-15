import heapq

def ucs(graph, start, goal):
    # (cost, node)
    priority_queue = []
    heapq.heappush(priority_queue, (0, start))

    visited = set()
    cost_so_far = {start: 0}
    parent = {start: None}

    while priority_queue:
        current_cost, current_node = heapq.heappop(priority_queue)

        if current_node in visited:
            continue

        visited.add(current_node)

        # Goal reached
        if current_node == goal:
            path = []
            while current_node is not None:
                path.append(current_node)
                current_node = parent[current_node]

            path.reverse()
            print("Minimum Cost:", current_cost)
            print("Path:", path)
            return

        # Explore neighbors
        for neighbor, weight in graph[current_node]:
            new_cost = current_cost + weight

            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                cost_so_far[neighbor] = new_cost
                heapq.heappush(priority_queue, (new_cost, neighbor))
                parent[neighbor] = current_node

    print("No path found")


# Example graph
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2), ('E', 5)],
    'C': [('F', 1)],
    'D': [],
    'E': [('F', 1)],
    'F': []
}

# Call function
ucs(graph, 'A', 'F')
