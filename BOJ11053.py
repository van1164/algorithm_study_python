a = int(input())
lst = list(map(int,input().split()))
dp = []
for i in range(a):
    maxx = 0
    for j in range(i+1):
        if dp:
            if lst[j]<lst[i] and dp[j]>maxx:
                maxx = dp[j]
    dp.append(maxx+1)
print(max(dp))