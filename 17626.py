import math


n = int(input())
check = n

li = [i**2 for i in range(1, 224)]
li.sort(reverse=True)

idx = 0
cnt = 0
res = 0

