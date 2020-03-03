import sys
from collections import deque

m,n = map(int, sys.stdin.readline().split())
matrix = []
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
is_visited = [[False] * m for i in range(n)]
day = 0

for i in range(n):
    matrix.append(list(map(int, sys.stdin.readline().split())))

def bfs(x,y):
    dq = deque()
    dq.append((x,y))
    matrix[x][y] = 1
    global day

    while dq:
        x,y = dq.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx<0 or nx>= m or ny<0 or ny>=n:
                continue
            if matrix[nx][ny] == 0 and is_visited[nx][ny] == False:
                matrix[nx][ny] = 1
                is_visited[nx][ny] = 1
                dq.append((nx,ny))
    day += 1

