import sys

li = list()

for i in range(9):
    li.append(int(sys.stdin.readline().strip()))

res = list()

for i in range(0, len(li)-1):
    temp = li[:]
    temp[i] = 0
    for j in range(i+1, len(li)):
        b = temp[j]
        temp[j] = 0
        if sum(temp) == 100:
            res = temp
            break
        else:
            temp[j] = b

for elem in res:
    if elem > 0:
        print(elem)