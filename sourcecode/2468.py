import sys
sys.setrecursionlimit(10000)

n = int(input())

matrix = []
for i in range(n):
    temp = list(map(int, input().split()))
    matrix.append(temp)

_max = 0
_min = 101

for i in range(1, len(matrix)):
    if max(matrix[i]) > _max:
        _max = max(matrix[i])
    
    if min(matrix[i]) < _min:
        _min = min(matrix[i])

dx = [1,-1,0,0]
dy = [0,0,1,-1]

visited = [[False]*n for i in range(n)]

max_component = 1

def dfs(x,y, height, visited):
    visited[x][y] = True

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0<=nx<n and 0<=ny<n:
            if matrix[nx][ny] > height and visited[nx][ny] == False:
                dfs(nx, ny, height, visited)
    


def main(height):
    global max_component
    visited = [[False]*n for i in range(n)]
    component = 0

    for i in range(n):
        for j in range(n):
            if matrix[i][j] > height and visited[i][j] == False:
                component += 1
                dfs(i,j, height, visited)
    
    if component > max_component:
        max_component = component



for i in range(_min, _max+1):
    main(i)

print(max_component)