import sys

dx = [1,-1,0,0]
dy = [0,0,1,-1]
cnt = 0

def dfs(x,y):
    global cnt
    # 하나 방문
    matrix[x][y] = 0
    cnt += 1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx<0 or nx>=N or ny<0 or ny>=M:
            continue

        if matrix[nx][ny] == 1:
            dfs(nx, ny)

t = int(sys.stdin.readline().strip())

for i in range(t):
    M,N,K = map(int, sys.stdin.readline().split())
    matrix = [[0]*M for i in range(N)]
    for i in range(K):
        x,y = map(int, sys.stdin.readline().split())
        matrix[y][x] = 1
    

    res = []
    for i in range(N):
        for j in range(M):
            if matrix[i][j] == 1:
                cnt = 0
                dfs(i,j)
                res.append(cnt)
    
    







