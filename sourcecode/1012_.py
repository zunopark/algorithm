import sys

t = int(input())

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def dfs(x,y):
    visited[x][y] = True

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0<=nx<n and 0<=ny<m:
            if matrix[nx][ny] == 1 and visited[nx][ny] == False:
                visited[nx][ny] = True
                dfs(nx, ny)

while t>0:
    m,n,k = map(int, input().split())
    cnt = 0

    matrix = [[0]*m for i in range(n)]
    visited = [[False]*m for i in range(n)]

    for i in range(k):
        a,b = map(int, input().split())
        matrix[b][a] = 1

    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 1 and visited[i][j] == False:
                dfs(i,j)
                cnt += 1

    print(cnt)


    t -= 1