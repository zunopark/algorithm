n = int(input())

li = []

for i in range(n):
    temp = int(input())
    li.append(temp)

li.sort()

for elem in li:
    print(elem)