import sys

while True:
    n = int(input())
    if n == 0:
        break
    li = [i for i in range(n+1, 2*n+1)]
    check = [False] * n
    count = 0

    # 체 알고리즘

    