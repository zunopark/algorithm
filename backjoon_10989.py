n = int(input())
li = []

for i in range(n):
    li.append(int(input()))

li.sort()

for elem in li:
    print(elem)