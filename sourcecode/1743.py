    import sys
    sys.setrecursionlimit(10000)

    n,m,k = map(int, input().split())

    matrix = [[0]*m for i in range(n)]
    visited = [[False]*m for i in range(n)]

    dx = [1,-1,0,0]
    dy = [0,0,1,-1]

    for i in range(k):
        r,c = map(int, input().split())
        matrix[r-1][c-1] = 1


    count = 1

    def dfs(x,y):
        global count
        visited[x][y] = True

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<n and 0<=ny<m:
                if matrix[nx][ny]==1 and visited[nx][ny] == False:
                    count += 1
                    dfs(nx, ny)
        
        return count


    trash = []

    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 1 and visited[i][j] == False:
                temp = dfs(i,j)
                trash.append(temp)
                count = 1

    print(max(trash))