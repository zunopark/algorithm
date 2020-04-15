# def DFS(graph, start_node):
#     visited = list()
#     need_visit = list()
#     need_visit.append(start_node)

#     while need_visit:
#         node = need_visit.pop()
#         if node not in visited:
#             visited.append(node)
#             need_visit.extend(graph[node])
    
#     return visited

# def BFS(graph, start_node):
#     visited = list()
#     need_visit = list()
#     need_visit.append(start_node)

#     while need_visit: # 데이터가 다 순회했는지 아닌지를 판단
#         node = need_visit.pop(0)
#         if node not in visited:
#             visited.append(node)
#             need_visit.extend(graph[node]) # 제일 뒤에 리스트를 붙인다.
    
#     return visited





M,N,V = map(int, input().split())

matrix = [[0] * (N + 1) for _ in range(N + 1)]

for i in range(M):
    link = list(map(int, input().split()))
    matrix[link[0]][link[1]] = 1
    matrix[link[1]][link[0]] = 1


def dfs(current_node, matrix, visited):
    visited += [current_node]
    for search_node in range(len(matrix[current_node])):
        if matrix[current_node][search_node] and search_node not in visited:
            visited = dfs(search_node, matrix, visited)
    
    return visited

def bfs(start_node):
    queue = [start_node]
    visited = [start_node]

    while queue:
        current_node = queue.pop(0)
        for search_node in range(len(matrix[current_node])):
            if matrix[current_node][search_node] and search_node not in visited:
                visited += [search_node]
                queue += [search_node]
    
    return visited

print(*dfs(V, matrix, []))
print(*bfs(V))

# print(graph)

# print(DFS(graph, v))
# print(BFS(graph, v))

# graph = dict()
# graph['A'] = ['B', 'C']
# graph['B'] = ['A', 'D']
# graph['C'] = ['A', 'G', 'H', 'I']
# graph['D'] = ['B', 'E', 'F']
# graph['E'] = ['D']
# graph['F'] = ['D']
# graph['G'] = ['C']
# graph['H'] = ['C']
# graph['I'] = ['C', 'J']
# graph['J'] = ['I']

# print(DFS(graph, 'A'))
# print(BFS(graph, 'A'))

