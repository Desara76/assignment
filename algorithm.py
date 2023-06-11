import heapq

# djikstra's algorithm
def shortest_path(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    heap = [(0, start)]
    while heap:
        current_distance, current_node = heapq.heappop(heap)

        # Skip if already found a shorter path
        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node]:
            distance = current_distance + float(weight)

            if distances.get(neighbor) and distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(heap, (distance, neighbor))

    return distances