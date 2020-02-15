import sys

li = list()

for i in range(4):
    li.append(list(map(int, sys.stdin.readline().split())))

res = list()


for i in range(0, len(li)):
    current = li[i][1]-li[i][0]
    res.append(current)

temp = 0
final = []
for elem in res:
    if elem > 0:
        temp += elem
    else:
        final.append(temp)
        temp = 0

print(max(final))
    
