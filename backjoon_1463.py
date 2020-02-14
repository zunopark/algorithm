x = int(input())

count = 0
check = 1

while check != x:
    if check*3 <= x:
        check = check * 3
        count += 1
    elif check * 2 <= x:
        check = check * 2
        count += 1
    elif check + 1 <= x:
        check = check + 1
        count += 1

print(count)
    