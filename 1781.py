import heapq

n = int(input())
li = []
q = []

for i in range(n):
    a,b = map(int, input().split())
    li.append((a,b))

li.sort()

for elem in li:
    deadline = elem[0]
    heapq.heappush(q, elem[1])
    if deadline<len(q):
        heapq.heappop(q)

print(sum(q))