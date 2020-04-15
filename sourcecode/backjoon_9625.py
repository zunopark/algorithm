# B의 개수
li = [0 for i in range(45)]
li[0] = 0
li[1] = 1

def fibo_k(k):
    if k <= 1:
        return k
    else:
        li[k] = fibo_k(k-2) + fibo_k(k-1)
        return li[k]


k = int(input())
fibo_k(k)

print(li[k-1], li[k])









