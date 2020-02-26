import sys


def binary_search(list, value):
    if len(list) == 0:
        return False
    if len(list) == 1 and list[0] == value:
        return True
    if len(list) == 1 and list[0] != value:
        return False
    
    mid = len(list) // 2
    if value == list[mid]:
        return True
    else:
        if value < list[mid]:
            return binary_search(list[:mid], value)
        else:
            return binary_search(list[mid:], value)

n = int(input())
a = list(map(int, sys.stdin.readline().split()))

m = int(input())
b = list(map(int, sys.stdin.readline().split()))

a.sort()

for elem in b:
    if binary_search(a, elem):
        print(1)
    else:
        print(0)

