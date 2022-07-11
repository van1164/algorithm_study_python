import sys
import heapq
def dijk(graph,start,end,N):
    distances =[100000000000000]*(N+1)
    distances[start] = 0
    
    que = [(0,start)]
    
    while que:
        time,n = heapq.heappop(que)
        if distances[n]<time:
            continue
        for new_time, new in graph[n]:
            dis = new_time + time
            if dis < distances[new]:
                distances[new] = dis
                heapq.heappush(que,(dis,new))
    return distances[end]


N= int(sys.stdin.readline())
M = int(sys.stdin.readline())
graph = [[] for _ in range(N+1)]
for i in range(M):
    s,e,t = list(map(int,sys.stdin.readline().split()))
    graph[s].append((t,e))
start,end =  list(map(int,sys.stdin.readline().split()))
print(dijk(graph,start,end,N))