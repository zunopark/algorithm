import sys
sys.setrecursionlimit(10000)

n,m = map(int, input().split())

graph = [[] for i in range(n+1)]
visited = [False] * (n+1)
result = 0


for i in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(b)

def dfs(start_node):
    visited[start_node] = True

    for elem in graph[start_node]:
        if visited[elem] == False:
            dfs(elem)


for i in range(1, n+1):
    if visited[i] == False:
        dfs(i)
        result += 1

print(result)