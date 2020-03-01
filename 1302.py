import operator

N = int(input())

res = dict()

for i in range(N):
    temp = input()
    if temp not in res:
        res[temp] = 1
    else:
        res[temp] += 1

sdict= sorted(res.items(), key=operator.itemgetter(1), reverse=True)

top = sdict[0][1]
final = []

for elem in sdict:
    if elem[1] == top:
        final.append(elem[0])

final.sort()
print(final[0])

