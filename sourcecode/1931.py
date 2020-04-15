n = int(input())
li = []

for i in range(n):
    temp = list(map(int, input().split()))
    li.append(temp)

li.sort(key=lambda x: x[0])
li.sort(key=lambda x: x[1])
cnt = 1
flag = li[0][1]

for i in range(1, len(li)):
    if li[i][0] >= flag:
        cnt += 1
        flag = li[i][1]

print(cnt)



