from collections import deque
from math import ceil

N,M =list(map(int, input().split()))
lst = list(map(int, input().split()))
length = N
cnt =0
graph =deque([x for x in range(1,N+1)])
for i in lst:
    idx = graph.index(i)
    if idx<ceil(N/2):
        for i in range(idx):
            graph.append(graph.popleft())
            cnt+=1
        graph.popleft()
        N-=1
    else:
        for i in range(N-idx):
            graph.appendleft(graph.pop())
            cnt+=1
        graph.popleft()
        N-=1
        
print(cnt)