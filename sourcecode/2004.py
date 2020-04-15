import itertools

n,m = map(int, input().split())
li = [i for i in range(1,n+1)]

a = list(itertools.combinations(li, m))
temp = list(str(len(a)))
cnt = 0

for i in range(len(temp)-1, 0, -1):
    if temp[i] == '0':
        cnt += 1
    else:
        break

print(cnt)