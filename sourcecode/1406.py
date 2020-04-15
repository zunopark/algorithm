import sys

data = input()
n = int(input())

stack_1 = list(data)
stack_2 = []

for i in range(n):
    temp = list(map(str, sys.stdin.readline().split()))
    if temp[0] == 'L':
        if stack_1:
            a = stack_1.pop()
            stack_2.append(a)
        else:
            continue
    elif temp[0] == 'D':
        if stack_2:
            a = stack_2.pop()
            stack_1.append(a)
        else:
            continue
    elif temp[0] == 'B':
        if stack_1:
            stack_1.pop()
        else:
            continue
    elif temp[0] == 'P':
        stack_1.append(temp[1])

print("".join(stack_1) + "".join(stack_2))

