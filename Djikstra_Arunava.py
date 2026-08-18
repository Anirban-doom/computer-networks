import heapq

def dijkstra(graph, start):
    # Distance from start to every vertex
    distances = {vertex: float('inf') for vertex in graph}
    distances[start] = 0

    # Priority queue: (distance, vertex)
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        # Ignore outdated entries
        if current_distance > distances[current_vertex]:
            continue

        # Check all neighbours
        for neighbour, weight in graph[current_vertex]:
            distance = current_distance + weight

            # If a shorter path is found
            if distance < distances[neighbour]:
                distances[neighbour] = distance
                heapq.heappush(priority_queue, (distance, neighbour))

    return distances


# Graph represented using an adjacency list
graph = {
    'A': [('B', 4), ('C', 2)],
    'B': [('A', 4), ('C', 1), ('D', 5)],
    'C': [('A', 2), ('B', 1), ('D', 8), ('E', 10)],
    'D': [('B', 5), ('C', 8), ('E', 2)],
    'E': [('C', 10), ('D', 2)]
}

# Find shortest paths from A
start = 'A'
result = dijkstra(graph, start)

print("Shortest distances from", start)

for vertex, distance in result.items():
    print(vertex, ":", distance)
