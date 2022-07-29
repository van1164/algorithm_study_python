import sys
sys.setrecursionlimit(10**9)
global dx
global dy
dx = [0,0,-1,1]
dy = [1,-1,0,0]


def dfs(graph,start,N,M,result,cnt = 0,visited = [False]*26):
    visited[ord(graph[0][0])-65] = True
    cnt+=1
    global dx,dy
    if result[0]<cnt:
        result[0] = cnt
    
    n,m = start[0],start[1]
    for i in range(4):
        x = n+dx[i]
        y = m+dy[i]
        
        if 0<=x<N and 0<=y<M and not visited[ord(graph[x][y])-65]:
            visited[ord(graph[x][y])-65] = True
            dfs(graph,(x,y),N,M,result,cnt,visited)
            visited[ord(graph[x][y])-65] = False
    

N,M = list(map(int, input().split()))
graph = []
for i in range(N):
    graph.append(input())
result = [0]
dfs(graph,(0,0),N,M,result)
print(result[0])

