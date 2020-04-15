import sys

N = int(input())

def check(current, num):
    if current < num:
        return False
    else:
        return True

num = 1
current = N
cnt = 0

while True:
    if not check(current, num):
        num = 1
    if current == 0:
        break
    current -= num
    num += 1
    cnt += 1

print(cnt)

