data = list(input())

_max_num = 0
need = 0
check = []



for elem in data:
    if elem not in check:
        check.append(elem)
        temp = data.count(elem)
        if temp > _max_num:
            _max_num = temp
            need = int(elem)

if need == 6 or need == 9:
    if _max_num%2==0:
        print(_max_num//2)
    else:
        print(_max_num//2+1)
else:
    print(_max_num)

