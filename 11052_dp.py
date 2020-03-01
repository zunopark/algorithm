import sys

N = int(sys.stdin.readline().strip())
value = list(map(int, ((input().split()))))

dp = [0 for i in range(N+1)]

# dp[N] == N개를 살때 최대값
dp[1] = value[0]
dp[2] = value[1]
dp[3] = value[2]
dp[4] = value[3]

def solution(N, value):
    pass 





