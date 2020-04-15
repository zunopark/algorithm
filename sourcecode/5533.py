n = int(input())
li=[]

for i in range(n):
    temp = list(map(int, input().split()))
    li.append(temp)

res = []

idx = 0
for i in range(n):
    if idx == 3:
        break
    temp = []
    for j in range(n):
        try:
            temp.append(li[j][idx])
        except:
            break
    
    res.append(temp)

    idx += 1

final = [0] * n

for i in range(3):
    for j in range(n):
        if res[i].count(res[i][j]) == 1:
            final[j] += res[i][j]

for elem in final:
    print(elem)
