import sys
from collections import deque
import heapq

def dijk(graph,lst,start,N,M):
    distances = [1000000000000000 for _ in range(N+1)]
    distances[start] = 0
    
    que = [(0,start)]
    
    while que:
        time,n = heapq.heappop(que)
        if time>M:
            continue
        
        for new_time,new in graph[n]:
            if time+new_time<distances[new]:
                distances[new] = time+new_time
                heapq.heappush(que,(time+new_time,new))
    summ=0
    for x in range(len(distances)):
        if distances[x]<=M:
            summ+=lst[x]
    return summ
            
    
            


def bfs(graph,lst,start,M):
    stack = deque([(0,start)])
    visited = set()
    cnt = 0
    while stack:
        time,n = stack.popleft()
        if time>M:
            continue
        
        if n not in visited:
            visited.add(n)
            cnt+=lst[n]
            for t,x in graph[n]:
                stack.append((t+time,x))    
    return cnt

N,M,R = list(map(int,sys.stdin.readline().split()))
lst = deque(list(map(int,sys.stdin.readline().split())))
lst.appendleft(0)
graph =[[] for _ in range(N+1)]
for i in range(R):
    s,e,t = list(map(int,sys.stdin.readline().split()))
    graph[s].append((t,e))
    graph[e].append((t,s))
maxx =0
for start in range(1,N+1):
    temp = dijk(graph,lst,start,N,M)
    if maxx<temp:
        maxx =temp
        
print (maxx)