import sys

input = sys.stdin.readline

dx = [1,-1,0,0,0,0]
dy = [0,0,1,-1,0,0]
dz = [0,0,0,0,1,-1]



def bfs(x,y,z):
    queue = []
    queue.append((x,y,z))
    visited[x][y][z] = True

    minit = 0
    while queue:
        size = len(queue)

        for i in range(size):
            a,b,c = queue.pop(0)
            if matrix[a][b][c] == 'E':
                print('Escaped in', end=" ")
                print(minit, end=" ")
                print("minute(s).")
                return
            
            for j in range(6):
                nx = a + dx[j]
                ny = b + dy[j]
                nz = c + dz[j]
                if 0<=nx<l and 0<=ny<r and 0<=nz<c:
                    if matrix[nx][ny][nz] == '.' and visited[nx][ny][nz] == False:
                        visited[nx][ny][nz] = True
                        queue.append((nx,ny,nz))
        
        minit += 1
    
    print('Trapped!')



    
while True:
    l,r,c = map(int, input().split())

    if l == 0 and r == 0 and c == 0:
        break

    matrix = [[[]*c for i in range(r)] for j in range(l)]
    visited = [[[False]*c for i in range(r)] for j in range(l)]

    for i in range(l):
        matrix[i] = [list(map(str, input().strip())) for j in range(r)]
        input()
    
    for i in range(l):
        for j in range(r):
            for k in range(c):
                if matrix[i][j][k] == 'S':
                    bfs(i,j,k)




