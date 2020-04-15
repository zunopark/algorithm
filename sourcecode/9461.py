t = int(input())

for i in range(t):
    temp = int(input())
    dp = [0]*(temp+1)
    dp[1] = 1
    dp[2] = 1
    dp[3] = 1
    dp[4] = 2
    dp[5] = 2

    if temp<6:
        print(dp[temp])
    else:
        for i in range(6, temp+1):
            dp[i] = dp[i-5] + dp[i-1]
    
    print(dp[temp])