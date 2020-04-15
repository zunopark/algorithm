def get_12(num):
    temp = []
    while num:
        temp.append(num%12)
        num = num // 12
    return sum(temp)

def get_16(num):
    temp = []
    while num:
        temp.append(num%16)
        num = num // 16
    return sum(temp)

def get_10(num):
    temp = []
    while num:
        temp.append(num%10)
        num = num // 10
    return sum(temp)


for i in range(2992, 10000):
    if get_12(i) == get_10(i) and get_16(i) == get_10(i) and get_12(i)==get_16(i):
        print(i)