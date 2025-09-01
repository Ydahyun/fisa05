import sys
input = sys.stdin.readline

T = int(input().strip())
qs = [int(input().strip()) for _ in range(T)]

m = max(qs)  # 처리해야 할 최대 n
size = max(3, m)

dp = [0] * (size + 1)
dp[0] = 1
dp[1] = 1
dp[2] = 2
for i in range(3, size + 1):
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

for n in qs:
    print(dp[n])
