n = int(input())

def get_number(num):
    return int(0.5*num*(num+1)+1)


cnt = 0
while True:
    if n>=get_number(cnt) and n<get_number(cnt+1):
        break
    cnt += 1

check = get_number(cnt)
n = n - check

cnt += 1
down = 1

for i in range(n):
    cnt -= 1
    down += 1

print(cnt, end="")
print('/', end="")
print(down)
