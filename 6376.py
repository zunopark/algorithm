def solution(n):
    if n == 0:
        return 1
    temp = 1
    for i in range(1, n+1):
        temp = temp * i
    
    return 1 / temp

print('n e')
print('- -----------')
for i in range(10):
    print(i, end=" ")
    temp = 0
    for j in range(i+1):
        temp += solution(j)
    print(temp)

