n = int(input())

li = []
alp = [] # 등장하는 단어들의 앞글자만을 저장
count = []
res = []

for i in range(n):
    temp = input()
    li.append(temp)



for elem in li:
    if elem.startswith(elem[0]) not in alp:
        alp.append(elem[0])
    else:
        continue

count = set(alp)
for elem in count:
    if alp.count(elem) >= 5:
        res.append(elem)

if len(res) == 0:
    print('PREDAJA')

res.sort()
for elem in res:
    print(elem, end="")