x = int(input())

y = int(input())
c = int(input()) # 상한
d = int(input()) # 리터당 추가

p = int(input()) # 총 수도양

res = []

res.append(p*x)

if p<=c:
    res.append(y)
else:
    temp = y
    p -= c
    temp += p*d
    res.append(temp)

print(min(res))