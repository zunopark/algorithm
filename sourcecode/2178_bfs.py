from collections import deque
# dx[0], dy[0] => 오른쪽
# dx[1], dy[1] => 왼쪽
# dx[2], dy[2] => 아래
# dx[3], dy[3] => 위
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

n,m = map(int, input().split())
li = [list(map(int, list(input()))) for _ in range(n)]

queue = list()
is_visited = [[False]*m for i in range(n)]
dist = [[0]*m for i in range(n)]

# 시작점
queue.append((0,0))
is_visited[0][0] = True
dist[0][0] = 1

while queue:
    x, y = queue.pop(0)
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0<=nx<n and 0<=ny<m:
            if is_visited[nx][ny] == False and li[nx][ny] == 1:
                queue.append((nx, ny))
                dist[nx][ny] = dist[x][y] + 1
                is_visited[nx][ny] = True

print(dist[n-1][m-1])
