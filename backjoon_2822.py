li = []
check = list()
a = []
for i in range(8):
    temp = int(input())
    li.append(temp)

check = li[:]
li.sort()

res = 0

for i in range(1, 6):
    res += li[-i]
    a.append(li[-i])

print(res)

for elem in check:
    if elem in a:
        print(check.index(elem)+1, end=" ")

