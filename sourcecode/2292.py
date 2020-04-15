n = int(input())

cnt = 1
result = 1

if n == 1:
    print(0)
else:
    while result < n:
        result += cnt*6
        cnt += 1
    
    print(cnt)