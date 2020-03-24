num = int(input())
n = int(input())

for i in range(2):
    num = num // 10

temp = list(str(num))
temp.append('0')
temp.append('0')

temp = "".join(temp)
a = int(temp)

cnt = 0 
while True:
    if a % n == 0:
        break
    else:
        a += 1
        cnt += 1

if cnt < 10:
    print(0, end="")
    print(cnt)
else:
    print(cnt)