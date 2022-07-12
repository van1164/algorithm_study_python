import sys
import heapq

def dijk(graph,start,end,N):
    distances = [100000000000 for _ in range(N+1)]
    distances[start] 
    que = [(0,start,[start])]
    result = set()
    while que:
        time,n,visited = heapq.heappop(que)
        if time>distances[n]:
            continue
        if n == end:
            result = visited
        for new_time, new in graph[n]:
            dis = new_time + time
            if dis<distances[new]:
                distances[new] = dis
                heapq.heappush(que,(dis,new,visited+[new]))
    return result, distances[end]

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
graph = [[] for _ in range(N+1)]
for i in range(M):
    s,e,t = list(map(int,sys.stdin.readline().split()))
    graph[s].append((t,e))
    
start, end = list(map(int,sys.stdin.readline().split()))

result, time =dijk(graph,start,end,N)
print(time)
print(len(result))
for i in result:
    print(i,end=' ')