import sys


n = int(input())

queue = []

for i in range(n):
    temp = sys.stdin.readline().split()
    if len(temp)>1:
        num = temp[-1]
        state = temp[0]
    else:
        state = temp[0]
    
    if state == 'push':
        queue.append(int(num))
    elif state == 'pop':
        if len(queue) == 0:
            print(-1)
        else:
            a = queue.pop(0)
            print(a)
    elif state == 'size':
        print(len(queue))
    elif state == 'empty':
        if len(queue) == 0:
            print(-1)
        else:
            print(0)
    elif state == 'front':
        if len(queue)==0:
            print(-1)
        else:
            print(queue[0])
    elif state == 'back':
        if len(queue)==0:
            print(-1)
        else:
            print(queue[-1])
    