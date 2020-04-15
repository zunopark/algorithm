n,m,v = map(int, input().split())

matrix = [[] for i in range(n+1)]
visited_dfs = []
visited_bfs = []

for i in range(m):
    a,b = map(int, input().split())
    matrix[a].append(b)
    matrix[b].append(a)

for elem in matrix:
    elem.sort()

def dfs(v):
    visited_dfs.append(v)
    print(v, end=" ")

    for elem in matrix[v]:
        if elem not in visited_dfs:
            dfs(elem)

def bfs(v):
    queue = []
    queue.append(v)
    visited_bfs.append(v)
    while queue:
        temp = queue.pop(0)
        print(temp, end=" ")
        for elem in matrix[temp]:
            if elem not in visited_bfs:
                visited_bfs.append(elem)
                queue.append(elem)



dfs(v)
print('')
bfs(v)