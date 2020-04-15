import sys

n = int(input())
li = []

for i in range(n):
    temp = list(map(int, sys.stdin.readline().split()))
    li.append(temp)


table = [li[i][1] if li[i][0] + i - 1 < n  else 0  for i in range(n)]

for date in range(n):
    if table[date] == 0:
        continue

    for prev in range(date):
        if li[prev][0] + prev - 1 < date:
            table[date] = max(table[prev]+li[date][1], table[date])

print(max(table))
