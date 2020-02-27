def BFS(graph, start_node):
    visited = list()
    need_visit = list()
    need_visit.append(start_node)

    while need_visit: # 데이터가 다 순회했는지 아닌지를 판단
        node = need_visit.pop(0)
        if node not in visited:
            visited.append(node)
            need_visit.extend(graph[node]) # 제일 뒤에 리스트를 붙인다.
    
    return visited
