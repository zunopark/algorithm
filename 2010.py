n = int(input())
li=[]
for i in range(n):
    li.append(int(input()))

res = 1

for elem in li:
    if elem == 1:
        continue
    else:
        res += elem-1

print(res)