import sys
input =sys.stdin.readline

t = int(input())
lst = list(map(int,input().split(" ")))
plus_dp = [-999999999]*(t+1)
maxx = -999999999
for i in range(t):
    plus_dp[i+1] = max(plus_dp[i]+lst[i],lst[i])
    maxx = max(plus_dp[i],maxx,lst[i])
    
print(max(plus_dp[t],maxx))