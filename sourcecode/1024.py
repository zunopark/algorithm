import sys
# 시간 초과 해결하기
N,L = map(int, input().split())


start = N // L - 1
res = start
i = 1

while True:
    res = res + (start + i)
    i += 1

    if i>=100:
        break

    if res > N:
        start = start - 1
        if start < 0:
            break
        res = start
        i = 1
    
    if res == N and i>=L:
        break

if i >= 100:
    print(-1)
    sys.exit()
elif start < 0:
    print(-1)
    sys.exit()
else:
    for i in range(i):
        print(start + i, end=" ")



