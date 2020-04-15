import sys

n = int(input())
li = list()

for i in range(n):
    li.append(int(sys.stdin.readline().strip()))

if li.count(0) > li.count(1):
    print('Junhee is not cute!')
else:
    print('Junhee is cute!')