n = int(input())

li = list(map(int, input().split()))

li.sort()

temp = list(set(li))
temp.sort()

print(len(temp))