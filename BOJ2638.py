import sys
from collections import deque


def bfs(graph,ones,N,M):
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    temp_graph = [[0]*M for _ in range(N)]
    for i in range(len(graph)):
        for j in range(len(graph[i])):
            temp_graph[i][j]=graph[i][j]
    temp_ones = deque([])
    while ones:
        a,b = ones.popleft()
        cnt = 0
        for i in range(4):
            x =a +dx[i]
            y = b+dy[i]
            if temp_graph[x][y]==2:
                cnt+=1
        if cnt>=2:
            graph[a][b]=2
        else:
            temp_ones.append((a,b))
    return temp_ones            

def make_air(graph,N,M):
    stack = deque([(0,0)])
    graph[0][0] = 2
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    visited = set()
    visited.add((0,0))
    while stack:
        a,b = stack.popleft()
        for i in range(4):
            x = a+dx[i]
            y = b+dy[i]
            if 0<=x<N and 0<=y<M: 
                if graph[x][y] ==0:
                    graph[x][y]=2
                    stack.append((x,y))
                elif graph[x][y] ==2 and (x,y)not in visited:
                    visited.add((x,y))
                    stack.append((x,y))
    


N,M = list(map(int,sys.stdin.readline().split()))
graph = []
ones = deque([])
for i in range(N):
    lst = list(map(int,sys.stdin.readline().split()))
    graph.append(lst)
    for k in range(len(lst)):
        if lst[k]==1:
            ones.append((i,k))
time =0    
 
while ones:
    make_air(graph,N,M)
    ones = bfs(graph,ones,N,M)
    time+=1            

print(time)
