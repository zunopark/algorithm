n,a,b = map(int, input().split())

li = [i for i in range(n)]

def check_if_meet(a,b):
    if a % 2 == 0:
        if b == a+1:
            return True
        else:
            return False
    elif a % 2 == 1:
        if b == a-1:
            return True
        else:
            return False

cnt = 1
idx_a = a-1
idx_b = b-1

while not check_if_meet(idx_a, idx_b):
    cnt += 1
    idx_a = idx_a // 2
    idx_b = idx_b // 2

print(cnt)
