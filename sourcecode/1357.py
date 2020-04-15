x,y = map(int, input().split())

def rev(number):
    temp = list(str(number))
    if '0' not in temp:
        temp.reverse()
        return int("".join(temp))
    else:
        cnt = 0
        for i in range(len(temp)-1, 0, -1):
            if temp[i] == '0':
                cnt += 1
            else:
                break
        
        temp = temp[:len(temp)-cnt]
        temp.reverse()
        return int("".join(temp))


print(rev(rev(x)+rev(y)))