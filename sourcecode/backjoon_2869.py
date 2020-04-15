a,b,v = map(int, input().split())

day = 0

while True:
    day += 1
    v -= a
    if v == 0:
        break
    v += b

print(day)

