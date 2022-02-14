a = int(input())
lst = list(map(int,input().rstrip().split()))
dp =[0,lst[0]]
for i in range(2,a+1):
    dp.append(lst[i-1])
    for j in range(i):
        if dp[i]<dp[j]+dp[i-j]:
            dp[i] = dp[j]+dp[i-j]
print(dp[-1])