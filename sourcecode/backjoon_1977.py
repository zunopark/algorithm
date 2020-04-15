import sys

m = int(input())
n = int(input())

li = [i**2 for i in range(1, 101)]

res = []

for i in range(m, n+1):
    if i in li:
        res.append(i)

if len(res) == 0:
    print(-1)
else:
    print(sum(res))
    print(min(res))
