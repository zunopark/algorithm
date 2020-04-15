import itertools

n,m = map(int, input().split())

li = [i for i in range(1, n+1)]

a = list(itertools.permutations(li, m)) # 2개의 원소로 수열 만들기

for elem in a:
    for i in range(len(elem)):
        print(elem[i], end=" ")
    print('')