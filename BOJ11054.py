import sys
sys.setrecursionlimit(10**9)
global result
result =0
def dfs(graph,t,start=0,cnt=0,peak=False,last = 0):
    global result
    if cnt>result:
        result=cnt
    if t-start+1+cnt <result:
        return
    if start ==t+1:
        return
    
    for i in range(start,t):
        if peak == True:
            if last>graph[i]:
                dfs(graph,t,i+1,cnt+1,True,graph[i])
        else:
            if  not cnt or last<graph[i] :
                dfs(graph,t,i+1,cnt+1,True,graph[i])
                dfs(graph,t,i+1,cnt+1,False,graph[i])






t = int(input())
graph = list(map(int,input().split()))
dfs(graph,t)
print(result)