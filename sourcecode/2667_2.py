n = int(input())

matrix = []
dx = [1,-1,0,0]
dy = [0,0,-1,1]

for i in range(n):
    temp = list(input())
    matrix.append(temp)

visited = [[False]*n for i in range(n)]

component = 1

def dfs(x,y):
    global component
    visited[x][y] = True

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0<=nx<n and 0<=ny<n:
            if matrix[nx][ny] == '1' and visited[nx][ny] == False:
                component += 1
                dfs(nx,ny)

    return component



total = 0
result = []

for i in range(n):
    for j in range(n):
        if matrix[i][j] == '1' and visited[i][j] == False:
            temp = dfs(i,j)
            result.append(temp)
            total += 1
            component = 1

print(total)
result.sort()
for elem in result:
    print(elem)
