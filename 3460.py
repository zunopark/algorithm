t = int(input())


for i in range(t):
    li=[]
    num = int(input())
    while num:
        temp = num%2
        li.append(temp)
        num = num // 2

    for i in range(len(li)):
        if li[i] == 1:
            print(i, end=" ")