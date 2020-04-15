temp = input().split('-')

num = []

for elem in temp:
    cnt = 0
    a = elem.split('+')
    for b in a:
        cnt += int(b)
    num.append(cnt)

n = num[0]

for i in range(1, len(num)):
    n -= num[i]

print(n)