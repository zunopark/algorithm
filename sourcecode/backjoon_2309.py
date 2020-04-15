
def solution(li):
    for i in range(0, len(li)-1):
        for j in range(i+1, len(li)):
            check = li[:]
            check.remove(li[i])
            check.remove(li[j])
            if sum(check) == 100:
                return check

li = []

for i in range(9):
    temp = int(input())
    li.append(temp)

res = solution(li)
res.sort()
for elem in res:
    print(elem)