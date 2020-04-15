n = int(input())
li = []
for i in range(n):
    temp = list(map(int, input().split()))
    li.append(temp)


# dp[n] => n번째 집까지의 최소 비용

def solution(list, n, x):
    dp = [0] * 1000
    dp[0] = list[0][x]
    idx = list[0].index(dp[0])
    
    for i in range(1, len(list)):
        temp = []
        for j in range(0, 3):
            if j == idx:
                continue
            else:
                temp.append(list[i][j])
        
        a = min(temp)
        idx = list[i].index(a)
        dp[i] = dp[i-1] + a
    
    return dp[n-1]

res = []
res.append(solution(li, n, 0))
res.append(solution(li, n, 1))
res.append(solution(li, n, 2))

print(min(res))
