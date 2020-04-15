n,m = map(int, input().split())

matrix = []

for i in range(n):
    temp = list(input())
    matrix.append(temp)

visited = [[False]*m for i in range(n)]



dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs(x,y):
    queue = []
    queue.append((x,y))
    visited[x][y] = True

    level = 0
    while queue:
        size = len(queue)

        for i in range(size):
            a, b = queue.pop(0)
            if a == n-1 and b == m-1:
                print(level+1)
                return

            for j in range(4):
                nx = a + dx[j]
                ny = b + dy[j]
                
                if 0<=nx<n and 0<=ny<m:
                    if matrix[nx][ny] == '1' and visited[nx][ny] == False:
                        visited[nx][ny] = True
                        queue.append((nx, ny))
        
        level += 1

bfs(0,0)