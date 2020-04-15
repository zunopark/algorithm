n = int(input())

def make(num):
    temp = list(str(num))
    _sum = 0
    for elem in temp:
        _sum += int(elem)
    
    return num + _sum

check = False

for i in range(1, 1000000):
    if make(i) == n:
        check = True
        print(i)
        break

if not check:
    print(0)