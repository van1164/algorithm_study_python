t = int(input())
graph = list(map(int,input().split()))
up_dp =[0]*t
down_dp =[0]*t
up_dp[0]=1
down_dp[0]=1
for i in range(1,t):
    up_maxx = 1
    down_maxx =1
    for j in range(i):
        if graph[j] < graph[i]:
            if up_maxx < up_dp[j]+1:
                up_maxx = up_dp[j]+1
        elif graph[j]> graph[i]:
            temp = max(up_dp[j],down_dp[j])
            if down_maxx< temp+1:
                down_maxx = temp+1
    up_dp[i]=up_maxx
    down_dp[i]=down_maxx

            
print(max(max(up_dp),max(down_dp)))