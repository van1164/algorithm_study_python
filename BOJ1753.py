import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)
a, b = map(int, input().split())
start = int(input())
graph = dict()
for i in range(1,a+1):
    graph[i]=set()
distance = [INF]*(a+1)

for _ in range(b):
    x,y,z = map(int,input().split())
    graph[x].add((y,z))
    
def dijkstra(start):
    stack = []
    heapq.heappush(stack,(0,start))
    distance[start] = 0
    while stack:
        dist, now = heapq.heappop(stack)
        if distance[now]<dist:
            continue
        for i,j in graph[now]:
            cost = dist + j
            if cost<distance[i]:
                distance[i] = cost
                heapq.heappush(stack,(cost,i))
dijkstra(start)

for i in range(1,a+1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])