num = int(input())

def is_6(number):
    data = list(str(number))
    for i in range(1, len(data)-1, 1):
        if data[i] == '6' and data[i-1] == '6' and data[i+1] == '6':
            return True
    return False

li = []
cnt = 666

while True:
    if len(li) == num:
        print(li[-1])
        break
    if is_6(cnt):
        li.append(cnt)
    cnt += 1