import sys

n, m = sys.stdin.readline().split()

li = list()
res = list()

for i in range(int(n)+int(m)):
    temp = sys.stdin.readline().strip()
    if temp not in li:
        li.append(temp)
    else:
        res.append(temp)

res.sort()
print(len(res))
for elem in res:
    print(elem)

# for elem in li:
#     if li.count(elem) > 1:
#         if elem not in res:
#             res.append(elem)
#         else:
#             continue

# res.sort()
# print(len(res))
# for elem in res:
#     print(elem)