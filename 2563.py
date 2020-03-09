n = int(input())

num = 1
result = 0
sum = 0

while True:
    sum += num
    result += 1
    if sum>n:
        result -= 1
        break
    num += 1

print(result)