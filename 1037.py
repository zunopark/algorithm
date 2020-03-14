from math import gcd


n = int(input()) #약수의 개수
li = list(map(int, input().split())) # 1, N 제외한 약수들

li.sort()

print(li[0]*li[-1])