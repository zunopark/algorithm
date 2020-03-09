x = int(input())

cm = [64, 32, 16, 8, 4, 2, 1]
cnt = 0
i = 0

while x:
    if x-cm[i]>=0:
        x = x-cm[i]
        cnt += 1
    else:
        i += 1

print(cnt)