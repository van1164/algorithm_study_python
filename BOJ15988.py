t = int(input())
dp = {1:1,2:2,3:4}
for i in range(t):
    a = int(input())
    if a in dp:
        print(dp[a]%1000000009)
        continue
    for i in range(4,a+1):
        if i in dp:
            continue
        dp[i]=(dp[i-2]+dp[i-1]+dp[i-3])%1000000009
    print(dp[a]%1000000009)