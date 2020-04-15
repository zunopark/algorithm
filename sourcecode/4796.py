idx = 1
while True:
    l,p,v = map(int, input().split())

    if l == 0 and p == 0 and v == 0:
        break

    result = 0
    while v > 0:
        if l<v:
            result += l
            v -= l
            v -= (p-l)
        else:
            result += v
            break
    
    print('Case', end=" ")
    print(idx, end="")
    print(':', end=" ")
    print(result)
    idx += 1
