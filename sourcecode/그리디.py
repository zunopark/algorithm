# coin 문제

import sys

N = int(sys.stdin.readline().strip())

def solution(list, value):
    detail = []
    coin_count = 0
    for coin in list:
        num = value // coin
        coin_count += num
        value -= coin * num
        detail.append([coin, num])
    
    return coin_count, detail

li = [500,100,50,1]

print(solution(li, N))