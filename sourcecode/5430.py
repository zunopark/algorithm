import sys

t = int(input())

def R(li):
    li.reverse()

def D(li):
    li.pop(0)

for i in range(t):
    temp = input()
    n = int(input())

    if n == 0:
        data = input()
        li = []
    else:
        li = list(map(int, input()[1:-1].split(',')))
    
    
    for elem in temp:
        if elem == 'R':
            R(li)
        elif elem == 'D':
            if len(li) == 0:
                print('error')
                sys.exit()
            else:
                D(li)
    
    print(li)
    
