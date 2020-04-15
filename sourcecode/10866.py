import sys

n = int(input())

deque = []

for i in range(n):
    temp = sys.stdin.readline().split()
    state = temp[0]
    if state == 'push_front':
        num = temp[1]
        deque.insert(0, num)
    elif state == 'push_back':
        num = temp[1]
        deque.append(num)
    elif state == 'pop_front':
        if len(deque) == 0:
            print(-1)
        else:
            num = deque[0]
            print(num)
            del deque[0]
    elif state == 'pop_back':
        if len(deque) == 0:
            print(-1)
        else:
            num = deque.pop()
            print(num)
    elif state == 'size':
        print(len(deque))
    elif state == 'empty':
        if len(deque) == 0:
            print(1)
        else:
            print(0)
    elif state == 'front':
        if len(deque) == 0:
            print(-1)
        else:
            print(deque[0])
    elif state == 'back':
        if len(deque) == 0:
            print(-1)
        else:
            print(deque[-1])