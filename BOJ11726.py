a = int(input())

dp = {1:1,2:3}
for i in range(3,a+1):
    dp[i]=(2*dp[i-2]+dp[i-1])%10007
    del dp[i-2]
print(dp[a]%10007)
    