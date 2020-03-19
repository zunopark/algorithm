from collections import Counter


n = int(input())
li = list(map(int, input().split()))
m = int(input())
check = list(map(int, input().split()))


dict = dict(Counter(li))

for elem in check:
    if elem in dict.keys():
        print(dict[elem], end=" ")
    else:
        print(0, end=" ")