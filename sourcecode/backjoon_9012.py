def check2(data):
    stack = data
    res = []
    for elem in stack:
        if elem == '(':
            res.append(elem)
        else:
            if len(res) != 0:
                res.pop()
            else:
                res.append(')')
    
    if len(res) == 0:
        return True
    else:
        return False
    


n = int(input())

for i in range(n):
    temp = list(input())
    if check2(temp):
        print('YES')
    else:
        print('NO')