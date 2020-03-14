a,b = map(str, input().split())

a = list(a)
b = list(b)

def solution(str1, str2):
    res = 0
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            res += 1
    
    return res


while len(a) != len(b):
    check1 = a[:]
    check2 = a[:]

    first = b[0]
    end = b[-1]

    check1.insert(0, first)
    temp1 = solution(check1, b)

    check2.append(end)
    temp2 = solution(check2, b)

    if temp1<=temp2:
        a.insert(0, first)
    else:
        a.append(end)

print(solution(a,b))


    