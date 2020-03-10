import sys

n = int(input())
li = []

for i in range(n):
    temp = list(map(int, sys.stdin.readline().split()))
    li.append(temp)


i = 0
result = 0

while True:
    if i == len(li):
        break

    temp = 0
    idx = i
    while True:
        if idx == len(li)-1 and li[idx][0] != 1:
            break
        temp += li[idx][1]
        idx += li[idx][0]
        if idx >= len(li):
            break

    if temp > result:
        result = temp
    
    i += 1

print(result)

