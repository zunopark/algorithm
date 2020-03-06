import heapq # python은 min 힙이다. 가장 앞의 원소는 제일 작은 값이다.

graph = {
    'A':{'B':8, 'C':1, 'D':2},
    'B':{},
    'C':{'B':5, 'D':2},
    'D':{'E':3, 'F':5},
    'E':{'F':1},
    'F':{'A':5}
}

def dijkstra(graph, start):
    distance = {node:float('inf')for node in graph}
    distance[start] = 0

    queue = []
    heapq.heappush(queue, [distance[start], start])

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        # 추가적인 작업 방지
        if distance[current_node] < current_distance:
            continue

        # 알고리즘
        for adjacent, weight in graph[current_node].items():
            distances = current_distance + weight

            if distances < distance[adjacent]:
                distance[adjacent] = distances
                heapq.heappush(queue, [distances, adjacent])
        
    return distance

print(dijkstra(graph, 'A'))

