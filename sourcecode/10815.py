import sys

n = int(input())
li = list(map(int, sys.stdin.readline().split()))

m = int(input())
check = list(map(int, sys.stdin.readline().split()))


def solution(list, target):
    start = 0
    end = len(list) - 1

    while start<=end:
        mid = (start+end) // 2

        if list[mid] == target:
            return True
        else:
            if list[mid] > target:
                end = mid - 1
            else:
                start = mid + 1
    
    return False

li.sort()

for elem in check:
    if solution(li, elem):
        print(1, end=" ")
    else:
        print(0, end=" ")