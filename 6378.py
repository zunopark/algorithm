import sys


def solution(num):
    result = 0
    while num:
        result += num % 10
        num = num // 10
    return result

while True:
    temp = int(input())
    if temp == 0:
        break

    while len(list(str(temp))) != 1:
        temp = solution(temp)
    
    print(temp)