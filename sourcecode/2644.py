n = int(input())
a,b = map(int, input().split())
m = int(input())

matrix = [[] for i in range(n+1)]
visited = []


for i in range(m):
    temp1, temp2 = map(int, input().split())
    matrix[temp1].append(temp2)
    matrix[temp2].append(temp1)


def bfs(v):
    queue = []
    queue.append(v)
    visited.append(v)

    level = 0
    while queue:
        size = len(queue)

        for i in range(0, size):
            temp = queue.pop(0)
            if temp == b:
                print(level)
                return
            for elem in matrix[temp]:
                if elem not in visited:
                    visited.append(elem)
                    queue.append(elem)
        
        level += 1
        
    
    print(-1)


bfs(a)