import sys

n = int(input())
li = []

for i in range(9):
    li.append(int(sys.stdin.readline().strip()))

print(n-sum(li))