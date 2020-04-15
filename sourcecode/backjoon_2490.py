import sys

def check(li):
    if li.count(0) == 1:
        print('A')
    elif li.count(0) == 2:
        print('B')
    elif li.count(0) == 3:
        print('C')
    elif li.count(0) == 4:
        print('D')
    elif li.count(0) == 0:
        print('E')


li = []

for i in range(3):
    li.append(list(map(int, sys.stdin.readline().split())))


for elem in li:
    check(elem)