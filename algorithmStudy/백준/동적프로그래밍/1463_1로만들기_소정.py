N = int(input())
dp = [0] * (10 ** 6+1)
dp[2] = 1
dp[3] = 1
for i in range(4, N+1):
    count3 = 1e6
    count2 = 1e6
    if i % 3 == 0:
        count3 = dp[i//3]
    if i % 2 == 0:
        count2 = dp[i//2]
    dp[i] = min(count3, count2, dp[i-1]) + 1
print(dp[N])