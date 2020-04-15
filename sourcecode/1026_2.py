n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort(reverse=True)

result = 0

for i in range(len(a)):
    if a[i] == 0 or b[i] == 0:
        continue
    else:
        result += a[i] * b[i]

print(result)