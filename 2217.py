import heapq

n = int(input())
queue = []

for i in range(n):
    heapq.heappush(queue, int(input()))

print(queue)

w = n

