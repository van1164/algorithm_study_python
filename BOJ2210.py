
from collections import deque
import sys
sys.setrecursionlimit(10**9)

def dfs(graph,start,cnt,visited,string,result):
    dx = [0,0,1,-1]
    dy = [-1,1,0,0]
    print(start)
    if cnt==6:
        if not visited[int(string)]:
            visited[int(string)] = True
            result[0]+=1
            return
    
    for i in range(4):
        x = start[0]+dx[i]
        y = start[1]+dy[i]
        
        if 0<=x<5 and 0<=y<5:
            dfs(graph,(x,y),cnt+1,visited,string+graph[x][y],result)


graph = []

for i in range(5):
    graph.append(input().split())
result =[0]
visited = [False]*1000000
dfs(graph,(0,0),0,visited,'',result)
print(result[0])