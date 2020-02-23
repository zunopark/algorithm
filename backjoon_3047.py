import sys

li = list(map(int, sys.stdin.readline().split()))
order = list(input())

dict = {}

dict['C'] = max(li)
li.remove(max(li))
dict['B'] = max(li)
li.remove(max(li))
dict['A'] = max(li)

for elem in order:
    print(dict[elem], end=" ")
