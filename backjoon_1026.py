n = int(input())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

s = 0
temp_a = a[:]
temp_b = b[:]


for i in range(n):
    _max = max(temp_b)
    _min = min(temp_a)
    _max_idx = temp_b.index(_max)
    _min_idx = temp_a.index(_min)

    temp = a[_min_idx]
    a[_min_idx] = a[_max_idx]
    a[_max_idx] = temp

    temp_a.remove(_min)
    temp_b.remove(_max)

    print(temp_a, temp_b)

print(a)