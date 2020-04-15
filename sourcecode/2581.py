import sys

m = int(input())
n = int(input())

a = [False,False] + [True]*(n-1)
primes=[]

for i in range(2,n+1):
  if a[i]:
    primes.append(i)
    for j in range(2*i, n+1, i):
        a[j] = False


result = []
for elem in primes:
    if elem>=m and elem<=n:
        result.append(elem)
if len(result) == 0:
    print(-1)
else:
    print(sum(result))
    print(min(result))