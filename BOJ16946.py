import sys
from collections import deque
def bfs(graph,x,y,N,M):
    stack = deque([(x,y)])
    visited = set()
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    cnt =0
    while stack:
        n,m = stack.popleft()
        cnt+=1
        for i in range(4):
            x = n+dx[i]
            y = m + dy[i]
            if 0<=x<N and 0<=y<M and graph[x][y]==0 and (x,y) not in visited :
                visited.add((x,y))
                stack.append((x,y))
    return cnt

N,M = list(map(int,sys.stdin.readline().split()))
graph = []
byuk = []
result = []
for i in range(N):
    temp = sys.stdin.readline().rstrip()
    lst = []
    for p in temp:
        lst.append(int(p))
    for k in range(len(lst)):
        if lst[k]==1:
            byuk.append((i,k))
    graph.append(lst)
    result.append(lst)
for x,y in byuk:
    result[x][y] = bfs(graph,x,y,N,M)
    
    
for i in result:
    for j in i :
        print(j,end='')
    print()