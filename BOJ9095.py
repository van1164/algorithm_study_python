a = int(input())
dp = {1:1,2:2,3:4}
for i in range(4,11):
    dp[i]=(dp[i-2]+dp[i-1]+dp[i-3])
for i in range(a):
    print(dp[int(input())])