n = int(input())

count = 0
li = [0]*(n+1)

def solution(num):
    for i in range(2, num+1):
        li[i] = li[i-1] + 1
        if i%2==0:
            li[i] = min(li[i], li[i//2]+1)
        if i%3==0:
            li[i] = min(li[i], li[i//3]+1)
    
    return li[num]

print(solution(n))