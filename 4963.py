import sys

dx = [0, 1, -1, 0]
dy = [1, 0, 0, -1]
cnt = 0

def dfs(matrix, x, y, w, h):
    matrix[x][y] = 0 #방문

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx<0 or nx>=w or ny<0 or ny>=h:
            continue

        if matrix[nx][ny] == 1:
            dfs(matrix, nx, ny, w, h)
    

while True:
    w,h = map(int, input().split())
    if w == 0 and h == 0:
        break
    matrix = []
    for i in range(h):
        temp = list(map(int, input().split()))
        matrix.append(temp)
    

    for i in range(h):
        for j in range(w):
            if matrix[i][j] == 1:
                dfs(matrix, i,j, w, h)
                cnt += 1
    
    