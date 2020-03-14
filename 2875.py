n,m,k = map(int, input().split())


_min = min(min(n//2, m), (n+m-k)//3)
print(_min)