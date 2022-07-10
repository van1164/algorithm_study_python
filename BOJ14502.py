from itertools import combinations
import sys
from collections import deque
def bfs(graph,start,N,M):
    stack = deque([start])
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    while stack:
        a,b = stack.popleft()
        for i in range(4):
            x = a+dx[i]
            y = b+dy[i]
            if 0<=x<N and 0<=y<M and graph[x][y]==0:
                graph[x][y]=2
                stack.append((x,y))


N,M = list(map(int,sys.stdin.readline().split()))
graph = []
virus = []
zero = []
for i in range(N):
    lst = list(map(int,sys.stdin.readline().split()))
    for k in range(len(lst)):
        if lst[k] == 2:
            virus.append((i,k))
        elif lst[k] ==0:
            zero.append((i,k))
    graph.append(lst)
maxx=0
time = 0
for lst in combinations(zero,3):
    temp_sum = 0
    for x,y in lst:
        graph[x][y] =1
    for start in virus:
        bfs(graph,start,N,M)
    for i in graph:
        temp_sum +=i.count(0)
    if maxx <temp_sum:
        maxx = temp_sum
    for x,y in zero:
        graph[x][y]=0
print(maxx)
