import sys


def solution(li):
    hp = li[0] + li[4]
    if hp < 1:
        hp = 1
    mp = li[1] + li[5]
    if mp < 1:
        mp = 1
    at = li[2] + li[6]
    if at < 0:
        at = 0
    df = li[3] + li[7]

    return hp + 5*mp + 2*at + 2*df




n = int(input())

li = list()

for i in range(n):
    temp = list(map(int ,input().split()))
    li.append(temp)

for elem in li:
    print(solution(elem))
