import sys
import heapq

N,M = list(map(int,sys.stdin.readline().strip().split()))

graph = [[] for _ in range(N+1)]
visited = [False]*(N+1)
for i in range(M):
    s,e,t = list(map(int,sys.stdin.readline().strip().split()))
    heapq.heappush(graph[s],(t,e))
    heapq.heappush(graph[e],(t,s))

stack = graph[1]
heapq.heapify(stack)
cnt = 0
visited[1] = True
while stack:
    t,e = heapq.heappop(stack)
    if not visited[e]:
        visited[e] = True
        cnt+=t
    for new_t,new_e in graph[e]:
        if not visited[new_e]:
            heapq.heappush(stack,(new_t,new_e))
print(cnt)