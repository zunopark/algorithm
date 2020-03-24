import heapq
import sys

queue = []

n = int(sys.stdin.readline().strip())

for i in range(n):
    temp = int(sys.stdin.readline().strip())
    if temp != 0:
        heapq.heappush(queue, temp)
    elif temp == 0:
        if len(queue) == 0:
            print(0)
        else:
            print(heapq.heappop(queue))