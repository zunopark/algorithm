a,b,c = map(int, input().split())

#print(n%15, n%28, n%19)

year = 1

while True:
    if (year-a) % 15 == 0 and (year-b) % 28 == 0 and (year-c) % 19 == 0:
        break
    else:
        year += 1

print(year)