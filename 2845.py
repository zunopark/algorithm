a,b = map(int, input().split())

_sum = a*b

li = list(map(int, input().split()))

for elem in li:
    print(elem-_sum, end=" ")