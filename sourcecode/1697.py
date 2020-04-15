from collections import deque


n,k = map(int, input().split())
limit = 100001
li = [0] * limit

def bfs(li):
    dq = deque()
    dq.append(n)

    while dq:
        temp = dq.popleft()

        if temp == k:
            return li[temp]
        
        for i in (temp-1, temp+1, temp*2):
            if 0<=i<limit and li[i] == 0:
                li[i] = li[temp] + 1
                dq.append(i)

print(bfs(li))