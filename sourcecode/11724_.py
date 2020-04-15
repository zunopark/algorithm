import sys
sys.setrecursionlimit(10**6)

n,m = map(int, input().split())

matrix = [[] for i in range(n+1)]
visited = [False] * (n+1)
cnt = 0

for i in range(m):
    u,v = map(int, input().split())
    matrix[u].append(v)
    matrix[v].append(u)

def dfs(v):
    visited[v] = True
    for elem in matrix[v]:
        if visited[elem] == False:
            visited[elem] = True
            dfs(elem)

for i in range(1, len(matrix)):
    for j in range(len(matrix[i])):
        if visited[matrix[i][j]] == False:
            dfs(matrix[i][j])
            cnt += 1

print(cnt)