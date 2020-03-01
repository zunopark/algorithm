# 시간 초과 해결하기


N,L = map(int, input().split())

current = N // L - 1
start = current
sum = 0
res = []
empty = []

while True:
    for i in range(1, 100):
        sum += current
        res.append(current)
        current += 1
        if sum >= N:
            break
    if sum == N:
        print(res)
        break
    else:
        res = empty[:]
        start -= 1
        current = start - 1
        sum = 0

for elem in res:
    print(elem, end=" ")

        

