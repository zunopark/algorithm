n = int(input())

dp = [0] * 1000001

def solution(n):
    if n == 1:
        return 0
    if dp[n] != 0:
        return dp[n]
    
    result = solution(n-1) + 1

    if n % 3 == 0:
        result = min(result, solution(n//3)+1)
    
    if n % 2 == 0:
        result = min(result, solution(n//2)+1)
    
    dp[n] = result
    return result

print(solution(n))