def get_powerset(A):
    A_size = len(A)
    A_pow = []
    for i in range(2**A_size):
        flag = bin(i)[2:].zfill(A_size)
        subset = [A[j] for j in range(A_size) if flag[j] == '1']
        A_pow.append(subset)
    return A_pow

n,s = input().split()
li = list(map(int, input().split()))

cnt = 0
res = get_powerset(li)

for i in range(1, len(res)):
    if sum(res[i]) == int(s):
        cnt += 1

print(cnt)

