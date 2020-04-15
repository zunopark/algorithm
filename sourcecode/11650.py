n = int(input())

li = []

for i in range(n):
    a,b = map(int, input().split())
    li.append([a,b])


li.sort()
for elem in li:
    print(elem[0], elem[1])