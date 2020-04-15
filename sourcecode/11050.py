def fact():
    li = [0]*11
    li[1] = 1
    for i in range(2, 11):
        result = 1
        for j in range(1, i+1):
            result = result * j
        li[i] = result
    
    return li

n,k = map(int, input().split())

res = fact()

print(res[n]//(res[k]*res[n-k]))