import sys

a,b = map(str, input().split())

li = []

def solution_min(num):
    res = []
    for elem in list(num):
        if elem == '6':
            res.append('5')
        else:
            res.append(elem)
    
    return int("".join(res))

def solution_max(num):
    res = []
    for elem in list(num):
        if elem == '5':
            res.append('6')
        else:
            res.append(elem)
    
    return int("".join(res))


li.append(solution_min(a)+solution_min(b))
li.append(solution_max(a)+solution_max(b))

print(min(li), end=" ")
print(max(li))