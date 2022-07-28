import sys
from collections import deque


def bfs(graph,start,receive,N,visited):
    que =deque([start])
    visited[start] = True
    receive[start] =-1
    while que:
        n =que.popleft()
        for i in graph[n]:
            if not visited[i]:
                receive[i]-=1
                if receive[i]==0:
                    receive[i]=-1
                    print(i,end=' ')
                    visited[i] =True
                    que.append(i)
        


N,M = list(map(int,sys.stdin.readline().split()))
graph = [[] for _ in range(N+1)]
receive = [0]*(N+1)
for i in range(M):
    a,b = list(map(int,sys.stdin.readline().split()))
    graph[a].append(b)
    receive[b]+=1
receive[0]=-1
visited = [False]*(N+1)
while 0 in receive:
    start = receive.index(0)
    print(start,end=' ')
    bfs(graph,start,receive,N,visited)    
