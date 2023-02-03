import heapq
import sys

input = sys.stdin.readline
N,k = list(map(int,input().split()))

lst = list(map(int,input().split()))
heap = []
for i in range(N):
    heapq.heappush(heap,-lst[i])
    
for i in range(k-1):
    heapq.heappop(heap)
    
print(-heapq.heappop(heap))