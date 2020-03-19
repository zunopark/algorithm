def solution(num):
    res = 0
    length = len(list(str(num)))
    while num:
        temp = num % 10
        res += temp * (10 ** (length-1))
        num = num // 10
        length -= 1

    return res

while True:
    temp = int(input())
    if temp == 0:
        break
    a = solution(temp)
    if a == temp:
        print('yes')
    else:
        print('no')