import heapq

n,m = map(int, input().split())
li = list(map(int, input().split()))

# 우선순위 큐
positive = []
negative = []
largest = max(max(li), -min(li))

# 최대 힙을 위해 원소를 음수로서
for elem in li:
    if elem>0:
        heapq.heappush(positive, -elem)
    else:
        heapq.heappush(negative, elem)

result = 0

while positive:
    result += heapq.heappop(positive)
    for i in range(m-1):
        if positive:
            heapq.heappop(positive)

while negative:
    result += heapq.heappop(negative)
    for i in range(m-1):
        if negative:
            heapq.heappop(negative)

print((-result)*2-largest)