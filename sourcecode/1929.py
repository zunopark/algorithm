def solution(num):
    a = set([i for i in range(3, num+1, 2)])
    for i in range(3, num+1, 2):
        if i in a:
            a -= set([i for i in range(i**2, num+1, i)])
    res = list(a)
    res.insert(0, 2)
    return res

n,m = map(int, input().split())

li = solution(m)

for elem in li:
    if elem >= n:
        print(elem)
