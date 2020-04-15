import sys


def solution(list):
    y = list[0] / list[1]
    return 1000 * y


x,y = map(int, input().split())
n = int(input())
li = []
res = []

for i in range(n):
    temp = list(map(int, sys.stdin.readline().split()))
    li.append(temp)

for elem in li:
    res.append(solution(elem))

print(round(min(res), 2))

