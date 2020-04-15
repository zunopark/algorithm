import sys
import math

def check(num):
    if num <= w or num <= h or num <= math.sqrt(w**2 + h**2):
        return True
    else:
        return False

n,w,h = (map(int, sys.stdin.readline().split()))
li = []
for i in range(n):
    li.append(int(input()))



for elem in li:
    if check(elem):
        print('DA')
    else:
        print('NE')


