n = int(input())

li = list(map(int, input().split()))

li = list(set(li))

li.sort()

for elem in li:
    print(elem, end=" ")