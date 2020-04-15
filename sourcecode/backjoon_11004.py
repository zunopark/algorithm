import sys

n,k = map(int, input().split())

li = list(map(int, sys.stdin.readline().split()))
li.sort()

print(li[k-1])