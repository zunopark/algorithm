# import sys

# dx = [0, 1, -1, 0]
# dy = [1, 0, 0, -1]

# n = int(sys.stdin.readline())
# matrix = [list(sys.stdin.readline()) for i in range(n)]
# cnt = 0
# apt = []

# def dfs(x,y):
#     global cnt
#     # 방문
#     matrix[x][y] = '0'
#     cnt += 1

#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]
#         if nx<0 or nx>=n or ny<0 or ny>=n:
#             continue
#         if matrix[nx][ny] == '1':
#             dfs(nx, ny)

# for i in range(n):
#     for j in range(n):
#         if matrix[i][j] == '1':
#             cnt = 0
#             dfs(i,j)
#             apt.append(cnt)

# print(len(apt))
# apt.sort()
# for i in apt:
#     print(i)

import sys
from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
n = int(sys.stdin.readline())
a = [list(sys.stdin.readline()) for _ in range(n)]
apt = []

def bfs(i, j):
    dq = deque()
    dq.append((i,j))
    a[i][j] = '0'
    cnt = 1

    while dq:
        x,y = dq.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx<0 or nx>=n or ny<0 or ny>=n:
                continue
            if a[nx][ny] == 1:
                cnt += 1
                dq.append((nx, ny))
                a[nx][ny] = '0'


for i in range(n):
    for j in range(n):
        if a[i][j] == '1':
            apt.append(bfs(i, j))

print(len(apt))
apt.sort()
for i in apt:
    print(i)


            

