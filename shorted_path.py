import heapq

def dijkstra(graph, start):
    
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0

    pq = [(0, start)]
    
    previous = {vertex: None for vertex in graph}

    while pq:
        current_distance, current_vertex = heapq.heappop(pq)

        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex]:
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous[neighbor] = current_vertex 
                heapq.heappush(pq, (distance, neighbor))

    return distances, previous

def shortest_paths(graph, start):
    distances, previous = dijkstra(graph, start)
    result = []
    
    for destination, distance in distances.items():
        path = []
        current = destination
        
        while current is not None:
            path.append(current)
            current = previous[current]
        
        path = path[::-1]
        
        result.append((f"{start} -> {destination}: {distance} Path: {'-'.join(path)}"))
    
    return result

graph = {
    'A': [('B', 4), ('C', 2)],
    'B': [('C', 5), ('D', 10)],
    'C': [('D', 3), ('E', 4)],
    'D': [('E', 1)],
    'E': []
}

start_node = 'A'
shortest_paths_result = shortest_paths(graph, start_node)

print("Shortest paths from A:")
for path_info in shortest_paths_result:
    print(path_info)