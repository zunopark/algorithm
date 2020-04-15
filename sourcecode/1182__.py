n = int(input())
li = []
result = 0

for i in range(n):
    li.append(float(input()))

def solution(li):
    global result
    for i in range(0, len(li)):
        _sum = 1
        for j in range(i, len(li)):
            _sum *= li[j]
            if _sum > result:
                result = _sum

solution(li)
print(round(result, 3))