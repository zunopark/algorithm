def get_num(data, li):
    temp = li[:]
    temp.remove(data)
    better = 1
    for elem in temp:
        if elem[1] > data[1]:
            better += 1
        elif elem[1] == data[1]:
            if elem[2] > data[2]:
                better += 1
            elif elem[2] == data[2]:
                if elem[3] > data[3]:
                    better += 1
                elif elem[3] == data[3]:
                    continue
    print(better)



n, k = input().split()

li = list()

for i in range(int(n)):
    temp = list(map(int, input().split()))
    li.append(temp)


get_num(li[int(k)-1], li)