import sys
import heapq

def bfs(dic,start):
    que = []
    dijk = [100*(N+1)]*(N+1)
    heapq.heapify(que)
    heapq.heappush(que,(0,start))
    dijk[start] = 0
    
    while que:
        n,now = heapq.heappop(que)

        if dijk[now]<n:
            continue
        for name,w in dic[now]:
            cost = n+w
            if cost<dijk[name]:
                dijk[name]=cost
                heapq.heappush(que,(cost,name))
    return dijk

N,M,X = list(map(int,sys.stdin.readline().split()))
dic = dict()
for i in range(M):
    dic[i+1] = list()
for i in range(M):
    a,b,c = list(map(int,sys.stdin.readline().split()))
    dic[a].append((b,c))
distance = [0]*(N+1)
for i in range(1,N+1):
    tmp = bfs(dic,i)
    distance[i] = tmp[X]
    
tmp = bfs(dic,X)
for i in range(1,N+1):
    distance[i]+=tmp[i]
    
print(max(distance))