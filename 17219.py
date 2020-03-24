import sys

n,m = map(int, input().split())

dict = {}

for i in range(n):
    temp = sys.stdin.readline().split()
    dict[temp[0]] = temp[1]

for i in range(m):
    temp = sys.stdin.readline().strip()
    print(dict[temp])
