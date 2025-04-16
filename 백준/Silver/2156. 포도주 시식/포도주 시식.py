n = int(input())

n_list = [int(input()) for _ in range(n)]

dp = [0]*10000

if n == 1:
    print(n_list[0])
elif n == 2:
    print(n_list[0] + n_list[1])
else:
    dp[0] = n_list[0]
    dp[1] = n_list[0] + n_list[1]
    dp[2] = max(dp[1], n_list[0] + n_list[2], n_list[1] + n_list[2])
    for i in range(3, n):
        dp[i] = max(dp[i-1], dp[i-2] + n_list[i], dp[i-3] + n_list[i-1] + n_list[i])
    print(dp[n-1])
