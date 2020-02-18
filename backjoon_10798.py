li=list()
res = []

for i in range(5):
    temp = list(input())
    li.append(temp)

max_len = 0
for elem in li:
    max_len += len(elem)

for i in range(max_len):
    if len(li[0]) != 0:
        res.append(li[0].pop(0))
    if len(li[1]) != 0:
        res.append(li[1].pop(0))
    if len(li[2]) != 0:
        res.append(li[2].pop(0))
    if len(li[3]) != 0:
        res.append(li[3].pop(0))
    if len(li[4]) != 0:
        res.append(li[4].pop(0))

final = "".join(res)
print(final)