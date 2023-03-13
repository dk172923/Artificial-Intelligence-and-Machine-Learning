def dijkstra(graph, start):
    # Create a dictionary to store the distance of each vertex from the start vertex
    distances = {vertex: float('inf') for vertex in graph}
    distances[start] = 0

    # Create a list to store the unvisited vertices
    unvisited = list(graph.keys())

    while unvisited:
        # Find the unvisited vertex with the smallest distance
        current_vertex = min(unvisited, key=lambda vertex: distances[vertex])

        # Remove the current vertex from the unvisited list
        unvisited.remove(current_vertex)

        # Visit each neighbor of the current vertex
        for neighbor, weight in graph[current_vertex].items():
            distance = distances[current_vertex] + weight

            # If the distance to the neighbor vertex is shorter than the current distance, update it
            if distance < distances[neighbor]:
                distances[neighbor] = distance

    # Return the dictionary of distances
    return distances
graph = {
    'A': {'B': 10, 'C': 3},
    'B': {'C': 1, 'D': 2},
    'C': {'D':8,'B':4,'E': 2},
    'D': {'E':7},
    'E': {'D':9}
}
start = 'A'
distances = dijkstra(graph, start)
print(distances)  # {'A': 0, 'B': 1, 'C': 3, 'D': 4}

