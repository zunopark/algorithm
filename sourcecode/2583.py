import sys
sys.setrecursionlimit(10000)


m,n,k = map(int, input().split())

matrix = [[0]*n for i in range(m)]
visited = [[False]*n for i in range(m)]

dx = [1,-1,0,0]
dy = [0,0,1,-1]

for i in range(k):
    x1,y1,x2,y2 = map(int, input().split())

    for j in range(y2-y1):
        for k in range(x2-x1):
            matrix[(m-y2)+j][(x1)+k] = 1
    


total = 0
count = []
result = 1


def dfs(x,y):
    global result

    visited[x][y] = True

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0<=nx<m and 0<=ny<n:
            if matrix[nx][ny] == 0 and visited[nx][ny] == False:
                result += 1
                dfs(nx, ny)

    return result
    
for i in range(m):
    for j in range(n):
        if matrix[i][j] == 0 and visited[i][j] == False:
            total += 1
            temp = dfs(i,j)
            count.append(temp)
            result = 1

print(total)
count.sort()
for elem in count:
    print(elem, end=" ")
            
            

