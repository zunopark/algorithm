n = int(input())
m = int(input())

li = []

for i in range(m):
    temp = list(map(int, input().split()))
    li.append(temp)

check = []
res = []

for elem in li:
    if 1 in elem:
        if elem[0] != 1:
            check.append(elem[0])
            res.append(elem[0])
        if elem[1] != 1:
            check.append(elem[1])
            res.append(elem[1])


for elem in li:
    if elem[0] in check:
        if elem[1] not in res:
            res.append(elem[1])
    if elem[1] in check:
        if elem[0] not in res:
            res.append(elem[0])
        

print(len(res)-1)