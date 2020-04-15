n = int(input())

cases = [i for i in range(111, 1000)]

def ridout(data):
    temp = list(str(data))

    for elem in temp:
        if temp.count(elem) > 1 or elem == '0':
            return True
    
    return False

possible = []

for elem in cases:
    if not ridout(elem):
        possible.append(elem)

def get(number, answer):
    case = list(str(answer))
    check = list(str(number))

    strike = 0
    ball = 0

    for i in range(3):
        if case[i] == check[i]:
            strike += 1
        else:
            if case[i] in check:
                ball += 1
    
    return strike, ball


cand = []

for i in range(n):
    number, strike, ball = map(int, input().split())
    cand.append([number, strike, ball])

cnt = 0

for elem in possible:
    check = True
    for c in cand:
        strike = c[1]
        ball = c[2]

        s, b = get(elem, c[0])
        if s != strike or b != ball:
            check = False
    
    if check:
        cnt += 1

print(cnt)







