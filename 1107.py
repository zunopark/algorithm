n = int(input())
m = int(input())

current = 100

if m>0:
    button = list(map(int, input().split()))
else:
    button = []

channel = []

for i in range(1, 1000001):
    check = True
    for elem in str(i):
        if elem in button:
            check = False
            break
    if check:
        channel.append(i)

min_diff = 987654321
value = ''
for elem in channel:
    if abs(elem-n)<min_diff:
        min_diff = abs(elem-n)
        val = str(elem)

answer = len(val) + abs(min_diff)
answer = min(answer, abs(n-current))
print(answer)
