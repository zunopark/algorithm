import heapq
import sys

n = int(input())
queue = []

for i in range(n):
    temp = int(sys.stdin.readline().strip())
    if temp != 0:
        heapq.heappush(queue, abs(temp))
    else:
        try:
            heapq.heappop(queue)
        except:
            print(0)
