li = []

for i in range(9):
    li.append(int(input()))

_sum = sum(li)
num1 = 0
num2 = 0


for i in range(0, 8):
    for j in range(i+1, 9):
        if _sum - (li[i]+li[j]) == 100:
            num1 = li[i]
            num2 = li[j]
            break

li.remove(num1)
li.remove(num2)

li.sort()

for elem in li:
    print(elem)

