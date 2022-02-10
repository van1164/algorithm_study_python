import sys
a = int(input())
dp = [1,1,1,2,2,3,4,5,7,9]
for i in range(10,101):
    dp.append(dp[i-5]+dp[i-1])
    
for i in range(a):
    x = int(input())
    print(dp[x-1])