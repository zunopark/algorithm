import heapq

n = int(input())

queue = []

for i in range(n):
    temp = int(input())
    if temp == 0:
        if len(queue) == 0:
            print(0)
        else:
            a = heapq.heappop(queue)
            print(-a)
    else:
        heapq.heappush(queue, -temp)


