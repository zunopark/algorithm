import sys

n = int(input())
li = []

for i in range(n):
    temp = list(map(int, sys.stdin.readline().split()))
    li.append(temp)

result = 0

for i in range(len(li)):
    temp = 0
    start_idx = i
    while start_idx < len(li):
        if start_idx == len(li)-1 and li[start_idx][0]>1:
            break
        temp += li[start_idx][1]
        start_idx += li[start_idx][0]
    if temp > result:
        result = temp

print(result)



