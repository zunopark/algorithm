import sys

def isprime(numlist, n):
    for i in range(2, n//2+1):
        if n % i == 0:
            numlist[i] = True

n,k = map(int, input().split())

numlist = [True for i in range(2, n+1)]

cnt = 0

for i in range(2, n+1):
    for j in range(i, n+1):
        if isprime(numlist, j) == False:
            continue
        numlist[j] = False
        cnt += 1
        if cnt == k:
            print(j+1)
            exit()



