n,m = map(int, input().split())

li = []
dict = {}

for i in range(n):
    temp = input()
    li.append(temp)
    dict[temp] = i + 1

for i in range(m):
    temp = input()
    if temp.isdigit():
        print(li[int(temp)-1])
    else:
        print(dict[temp])