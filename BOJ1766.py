import sys
from collections import deque

def bfs(graph,start,receive,N,visited):
    stack = deque([start])
    visited[start] = True
    receive[start]=-1
    while stack:
        n = stack.popleft()
        found = False
        for i in graph[n]:
            if not visited[i]:
                receive[i]-=1
                if receive[i]==0 and not found:
                    receive[i] = -1
                    print(i,end =' ')
                    visited[i]=True
                    stack.append(i)
                    found= True

N,M = list(map(int, sys.stdin.readline().split()))
receive = [0]*(N+1)
receive[0]=-1
graph = [[] for _ in range(N+1)]
for i in range(M):
    x,y = list(map(int, sys.stdin.readline().split()))
    graph[x].append(y)
    receive[y]+=1
    
for i in range(N):
    graph[i].sort()
visited = [False]*(N+1)
while 0 in receive:
    start = receive.index(0)
    print(start,end=' ')
    bfs(graph,start,receive,N,visited)
