import sys

def solution(list):
    temp = list.sort()
    return list[-1] + list[-2] + list[-3]

li = [int(sys.stdin.readline().strip()) for i in range(20)]

a = li[:10]
b = li[10:]

print(solution(a), solution(b))

