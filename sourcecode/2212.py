import sys

n = int(input())
k = int(input())

li = list(map(int, input().split()))
li.sort()

if k>=n:
    print(0)
    sys.exit()


cha = []
for i in range(len(li)-1):
    cha.append(li[i+1]-li[i])

for i in range(k-1):
    cha.remove(max(cha))

print(sum(cha))