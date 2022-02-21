from collections import deque
def bfs(graph,start):
    stack = deque([start])
    visited = set()
    boo =False
    while stack:
        n = stack.popleft()
        if n not in visited:
            if  n != start:
                visited.add(n)
            if start in graph[n]:
                boo =True
            stack += graph[n] - visited
    if boo:
        visited.add(start)
    return visited


a = int(input())
graph = {}
for i in range(1,a+1):
    graph[i] =set()
for i in range(1,a+1):
    lst =[x for x in enumerate(list(map(int,input().split()))) if x[1]==1]
    for j in lst:
        graph[i].add(j[0]+1)
for i in range(1,a+1):
    tmp = bfs(graph,i)
    for j in range(1,a+1):
        if j in tmp:
            print(1,end=' ')
        else:
            print(0,end=' ')
    print()