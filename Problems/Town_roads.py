import heapq

def dijkstra(graph, start, end):
    # Create a dictionary to store the shortest distances from the start node to each node.
    shortest_distances = {node: float('inf') for node in graph}
    shortest_distances[start] = 0

    # Create a priority queue to process nodes with the smallest tentative distances first.
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        # If we reached the destination node, return the shortest distance.
        if current_node == end:
            return shortest_distances[end]

        # Skip this node if we've already processed it.
        if current_distance > shortest_distances[current_node]:
            continue

        # Check all neighbors of the current node and update their tentative distances.
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < shortest_distances[neighbor]:
                shortest_distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    # If no path is found, return None.
    return None

# Define the graph with road distances.
graph = {
    'MH': {'BA': 22},
    'BA': {'MF': 9, 'BR': 29},
    'MF': {'BR': 42, 'BA': 9},
    'BR': {'IN': 91},
    'TF': {},
    'IN': {'BR': 91, 'DC': 39, 'LI': 6},
    'DC': {'IN': 39},
    'LI': {'IN': 6},
    'CH': {}
}


# Specify the starting and ending points.
start_point = 'MH'  
end_point = 'IN'    

# Find the shortest path distance.
shortest_distance = dijkstra(graph, start_point, end_point)

if shortest_distance is not None:
    print(f"The shortest distance from {start_point} to {end_point} is {shortest_distance} miles.")
else:
    print(f"There is no path from {start_point} to {end_point}.")
