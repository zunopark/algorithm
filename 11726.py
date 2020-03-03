import sys

n = int(sys.stdin.readline().strip())

li = [0] * 1001

li[1] = 1
li[2] = 2

if n <= 2:
    print(li[n])
else:
    for i in range(3, n+1):
        li[i] = li[i-1] + li[i-2]
    
    print(li[n]%10007)
    