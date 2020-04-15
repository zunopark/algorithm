import sys

n = int(input())
li = list(map(int, sys.stdin.readline().split()))

_max = 0
cha = []
res = []

for i in range(1, len(li)):
    cha.append(li[i]-li[i-1])
    
for i in range(len(cha)):
    if cha[i] > 0:
        _max += cha[i]
        if i == len(cha)-1:
            res.append(_max)
    elif cha[i] <= 0:
        res.append(_max)
        _max = 0


# 출력하는 부분
if sum(res) == 0:
    print('0')
else:
    print(max(res))