import itertools

n, m = map(int, input().split())

li = []

for i in range(1, n+1):
    li.append(str(i))

res = list(map(''.join, itertools.permutations(li, m)))

for elem in res:
    for elem2 in elem:
        print(elem2, end=" ")
    print('')