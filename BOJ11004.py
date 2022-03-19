import heapq
a,b =list(map(int,input().split()))
lst = list(map(int,input().split()))
queue = []
for i in lst:
    heapq.heappush(queue,i)
for i in range(b-1):
    heapq.heappop(queue)
print(heapq.heappop(queue))