t = int(input())


dx = [1,0,-1,0]
dy = [0,1,0,-1]

num = 1


def dfs(x,y):
    global num

    visited[x][y] = True
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0<=nx<n and 0<=ny<m:
            if matrix[nx][ny] == 1 and visited[nx][ny] == False:
                num += 1
                dfs(nx, ny)
    
    return num

def bfs(x,y):
    pass
    


while t>0:
    m, n, k = map(int, input().split())
    matrix = [[0]*m for i in range(n)]
    visited = [[False]*m for i in range(n)]
    cnt = 0

    for i in range(k):
        x,y = map(int, input().split())
        matrix[y][x] = 1
    
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 1 and visited[i][j] == False:
                cnt += 1
                a = dfs(i,j)
                print('배추의 개수', a)
                num = 1
    
    print(cnt)

    t -= 1