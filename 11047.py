n, k =map(int, input().split())
li = []

for i in range(n):
    li.append(int(input()))

check = k
li.sort(reverse=True)
cnt = 0
idx = 0
_sum = 0

while True:
    if li[idx] <= k:
        cnt += 1
        _sum += li[idx]
        k -= li[idx]
        if _sum == check:
            break
    else:
        idx += 1
        if idx == len(li):
            break

print(cnt)