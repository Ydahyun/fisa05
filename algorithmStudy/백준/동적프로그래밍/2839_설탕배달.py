N = int(input())

dp = [2000] * 5001

dp[3] = 1
dp[5] = 1


for i in range(N+1): # N개까지
    dp[i] = min(dp[i],dp[i-3]+1,dp[i-5]+1) # 현재 있는것과 3kg 전, 5kg전에 1스텝 더

if dp[N] < 2000:
    print(dp[N])
else:
    print(-1)

