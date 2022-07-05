from itertools import permutations
import sys
from collections import deque
import heapq

def bfs(graph,start,end,N):
    distances = [1000000000 for _ in range(N+1)]
    distances[start]=0
    que =[]
    heapq.heappush(que,(0,start))
    while que:
        time,s = heapq.heappop(que)
        
        if distances[s]<time:
            continue
        
        for new_time,new_S in graph[s]:
            dis = time+new_time
            if dis<distances[new_S]:
                distances[new_S]=dis
                heapq.heappush(que,(dis,new_S))
    return distances[end]
N,E = list(map(int,sys.stdin.readline().split()))
graph = [[] for _ in range(N+1)]
for i in range(E):
    s,e,t = list(map(int,sys.stdin.readline().split()))
    graph[s].append((t,e))
    graph[e].append((t,s))
v1, v2 = list(map(int,sys.stdin.readline().split()))
minn = 100000000000000



for a,b in permutations([v1,v2]):
    temp  = bfs(graph,1,a,N)
    temp += bfs(graph,a,b,N)
    temp+=bfs(graph,b,N,N)
    if minn >temp:
        minn = temp
if minn>100000000:
    print(-1)
else:
    print(minn)