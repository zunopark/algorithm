li = []

for i in range(5):
    temp = list(map(int, input().split()))
    li.append(temp)

_max = 0
i = 0
check = []

for i in range(0, 5):
    if sum(li[i]) > _max:
        _max = sum(li[i])
        check = li[i]

a = li.index(check)

print(a+1, _max)