li = [i for i in range(1, 31)]

for i in range(28):
    temp = int(input())
    li.remove(temp)

li.sort()

for elem in li:
    print(elem)