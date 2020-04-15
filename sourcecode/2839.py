import sys

num = int(input())

dp = [0] * (num+5)
dp[1] = -1
dp[2] = -1
dp[3] = 1
dp[4] = -1
dp[5] = 1

if num<=5:
    print(dp[num])
    sys.exit()
else:
    for i in range(6, num+1):
        if i == 7:
            dp[i] = -1
            continue
        dp[i] = 5000
        if i%3==0:
            dp[i] = i//3
        if i%5==0:
            dp[i] = i//5
        if i>=10:
            if dp[i-3] == -1 or dp[i-5] == -1:
                if dp[i-3] == -1:
                    dp[i] = min(dp[i], dp[i-5]+1)
                elif dp[i-5] == -1:
                    dp[i] = min(dp[i], dp[i-3]+1)
            else:
                dp[i] = min(dp[i], dp[i-3]+1, dp[i-5]+1)

print(dp[num])
        