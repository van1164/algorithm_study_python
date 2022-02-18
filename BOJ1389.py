from collections import deque
def bfs(graph,start,end):
    stack  = deque([start])
    visited = set()
    
    while stack:
        n = stack.popleft()
        if n[0] == end:
            return n[1]
        if n not in visited:
            visited.add(n[0])
            for i in graph[n[0]]:
                if i not in visited:
                    stack.append((i,n[1]+1))



a,b = list(map(int,input().split()))
graph = {}
for i in range(1,a+1):
    graph[i] = set()
for i in range(b):
    x,y = list(map(int,input().split()))
    graph[x].add(y)
    graph[y].add(x)
minn=100000000
minn_idx=150
for i in range(1,a+1):
    summ = 0
    for j in range(1,a+1):
        if j == i :
            continue
        summ += bfs(graph,(i,0),j)
    if summ <minn:
        minn = summ
        minn_idx = i

print(minn_idx)