import sys

def check(n):
    if n == 1:
        return False
    elif n == 2 or n == 3:
        return True
    else:
        for i in range(2, n//2+1):
            if n % i == 0:
                return False
        return True


n = int(sys.stdin.readline().strip())
li = list(map(int, sys.stdin.readline().split()))
cnt = n

for elem in li:
    if not check(elem):
        cnt -= 1

print(cnt)


