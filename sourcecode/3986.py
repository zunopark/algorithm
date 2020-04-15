n = int(input())


def solution(data):
    data = list(data)
    stack = []

    for elem in data:
        if len(stack) == 0:
            stack.append(elem)
        elif stack[-1] != elem:
            stack.append(elem)
        elif stack[-1] == elem:
            stack.pop()
    
    if len(stack) == 0:
        return 1
    else:
        return 0

case = []

for i in range(n):
    case.append(input())

cnt = 0
    
for elem in case:
    cnt += solution(elem)

print(cnt)
