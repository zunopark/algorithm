n = int(input())

matrix = []
visited = [[False]*n for i in range(n)]

total = 0
result = []
component = 1


dx=[1,-1,0,0]
dy=[0,0,1,-1]

def dfs(x,y):
    visited[x][y] = True
    global component

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0<=nx<n and 0<=ny<n:
            if matrix[nx][ny] == '1' and visited[nx][ny] == False:
                visited[nx][ny] = True
                component += 1
                dfs(nx,ny)
    
    return component



for i in range(n):
    temp = list(input())
    matrix.append(temp)


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

