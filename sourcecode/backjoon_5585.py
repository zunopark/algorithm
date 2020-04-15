n = int(input())

money = 1000 - n

coin = [500, 100, 50, 10, 5, 1]

cnt = 0

while n:
    if money-500 >= 0:
        money -= 500
        cnt += 1
        continue
    elif money-100 >= 0:
        money -= 100
        cnt += 1
        continue
    elif money-50 >= 0:
        money -= 50
        cnt += 1
        continue
    elif money-10 >= 0:
        money -= 10
        cnt += 1
        continue
    elif money-5 >= 0:
        money -= 5
        cnt += 1
        continue
    elif money-1 >= 0:
        money -= 1
        cnt += 1
        continue

print(cnt)
