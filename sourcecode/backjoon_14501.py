import sys

res = list()
n = int(input())
k = 1
check_sum = 0

for i in range(n):
    li = list(map(int, sys.stdin.readline().split()))
    res.append(li)


print(res)

for i in range(0, n, 1):
    _sum = 0
    for j in range(0, n, k):
        _sum += res[j][1]
        k = res[j][0]
    if _sum > check_sum:
        check_sum = _sum

print(check_sum)

