t = int(input())

check = False

def R(li):
    li.reverse()

def D(li):
    global check
    if li:
        li.pop(0)
    else:
        check = True

def solution(data, li):
    for elem in data:
        if elem == 'R':
            R(li)
        elif elem == 'D':
            D(li)


for i in range(t):
    data = list(input())
    n = int(input())
    temp = list(input())
    li = []

    for elem in temp:
        if elem.isdigit():
            li.append(int(elem))
    
    solution(data, li)
    
    if not check:
        print(li)
    else:
        print('error')
        check = False

