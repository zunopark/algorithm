from collections import deque


t = int(input())


while t>0:
    n, m = map(int, input().split())
    impotance = list(map(int, input().split()))
    dict = {}

    q = deque()
    for i in range(n):
        q.append(i)
        dict[i] = impotance[i]
    
    cnt = 1
    while q:
        temp = q.popleft()

        if temp == m:
            print(cnt)

        if dict[temp] == max(impotance):
            cnt += 1
            impotance.remove(max(impotance))
        else:
            q.append(temp)
    
    t -= 1



