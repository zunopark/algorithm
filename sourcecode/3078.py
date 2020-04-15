import sys

n,k = map(int, input().split())

li = []
check = []
cnt = 0

def solution(a, b):
    if a[1] == b[1] and b[2] - a[2] <= k:
        return True
    else:
        return False

for i in range(n):
    temp = sys.stdin.readline().strip()
    li.append((temp, len(temp), i))

for i in range(0, len(li)-1):
    if li[i] in check:
        continue
    for j in range(i+1, len(li)):
        if solution(li[i], li[j]):
            cnt += 1
            check.append(li[i])

print(cnt)






