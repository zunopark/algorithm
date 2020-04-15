n,k = map(int, input().split())

li = [i for i in range(1, n+1)]
res = []
idx = 0

while li:
    idx = (idx + k - 1) % len(li)
    res.append(li[idx])
    del li[idx]

print('<', end="")
for i in range(len(res)):
    if i == len(res)-1:
        print(res[i], end="")
        print('>')
    else:
        print(res[i], end=", ")
        