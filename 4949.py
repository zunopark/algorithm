while True:
    temp = list(input())
    if temp[0] =='.':
        break
    queue = list()
    for elem in temp:
        if elem == '(' or elem == '[':
            queue.append(elem)
        
        if len(queue) != 0:
            if elem == ')':
                top = queue[-1]
                if top == '(':
                    queue.pop()
            if elem == ']':
                top = queue[-1]
                if top == '[':
                    queue.pop()

    if len(queue) == 0:
        print('YES')
    else:
        print('NO')