import sys

n = int(sys.stdin.readline().strip())

li = []
for i in range(n):
    li.append(int(sys.stdin.readline().strip()))

res = 0
li.sort()

for i in range(len(li)):
    res += abs((i+1)-li[i])
    
print(res)