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

def solution(li, value):
    start = 0
    end = len(li)-1

    while start<=end:
        mid = (start+end)//2
        if li[mid] == value:
            return True
        else:
            if li[mid] > value:
                end = mid - 1
            else:
                start = mid + 1
    
    return False

n = int(input())
a = list(map(int, sys.stdin.readline().split()))

m = int(input())
b = list(map(int, sys.stdin.readline().split()))

a.sort()

for elem in b:
    if solution(a, elem):
        print(1)
    else:
        print(0)

