import sys
import heapq
N,M = list(map(int,sys.stdin.readline().split()))
visited = [0]*(N+1)
real=[False]*(N+1)
graph =[]

for i in range(M):
    s,e = list(map(int,sys.stdin.readline().split()))
    heapq.heappush(graph,(s,e))
    visited[e]+=1
i =1
print(visited)
while i<N+1:
    if visited[i]: # 처리할것이 있을 때
        i+=1
        continue
    else:
        if not real[i]:
            print(i,end=' ')
            real[i]=True

        while graph:
            start,end = heapq.heappop(graph)
            if start>i:
                heapq.heappush(graph,(start,end))
                i+=1
                break
            if not visited[start]:
                visited[end]-=1
                if end<i and not visited[end]:
                    i=1
                    break
            else:
                heapq.heappush(graph,(start,end))
                i+=1    
                break
    print(visited,graph)
                    
