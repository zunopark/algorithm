n,c = map(int, input().split())
li = []

for i in range(n):
    li.append(int(input()))

check = [False] * (c+1)
cnt = 0

for elem in li:
    for i in range(elem, c+1, elem):
        if not check[i]:
            check[i] = True
            cnt += 1

print(cnt)