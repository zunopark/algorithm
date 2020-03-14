import sys

def prime(n):
    if n == 2:
        return [2]
    tr = [True]*n

    m = int(n**0.5)

    for i in range(2, m+1):
        if tr[i] == True:
            for j in range(i+i, n, i):
                tr[j] = False
    
    return [i for i in range(2, n) if tr[i]==True]

while True:
    n = int(input())
    if n == 0:
        break

    li = prime(2*n)
    cnt = 0
    for elem in li:
        if elem > n and elem <= 2*n:
            cnt += 1
    
    print(cnt)