n = int(input())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

s = 0
temp_a = a[:]
temp_b = b[:]

res = [None] * n
_max = 0
_min = 0
_max_idx = 0
_min_idx = 0
_sum = 0

for i in range(0, n):
    _max = max(temp_b)
    _min = min(temp_a)
    _min_idx = temp_a.index(_min)
    _max_idx = temp_b.index(_max)

    res[_max_idx] = _min
    temp_a[_min_idx] = 101
    temp_b[_max_idx] = -1


for i in range(len(res)):
    _sum += res[i] * b[i]

print(_sum)