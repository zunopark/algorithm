import sys

n = int(input())

li = list()

for i in range(n):
    li.append(int(sys.stdin.readline().strip()))


print(li)

_max = max(li[0], li[1])
start_idx = li.index(_max)

for i in range(start_idx, len(li), 1):
    pass