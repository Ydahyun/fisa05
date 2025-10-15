T = int(input())

dp = []
#dp.append([1,2,3,4,5,6,7,8,9,10,11,12,13,14])



for _ in range(T):
    k = int(input())
    n = int(input())

    dp.append(list(range(1, n+1)))  # 0층

    for _ in range(k):
        dp.append([1]*n)

    for i in range(k):
        for j in range(n-1):
            dp[i+1][j+1] = dp[i+1][j] + dp[i][j+1]
            print(dp[i+1][j+1], dp[i+1][j] , dp[i][j+1])

    #print(dp)
    #print("+++++++++++++++++++")
    print(dp[k][n-1])
#print(dp)