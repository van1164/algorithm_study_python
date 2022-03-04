from collections import deque
def bfs(graph,start,visited):
    stack = deque([start])
    while stack:
        n = stack.popleft()
        for i in graph[n]: 
            if i not in visited:
                stack.append(i)
                visited.add(i)


a,b = list(map(int,input().split()))
visited = list(map(int,input().split()))
if visited[0] == 0:
    for i in range(b):
        input()
    print(b)
    exit()
visited = set(visited[1:])
graph = dict()
for i in range(1,a+1):
    graph[i] = set()
result = []
for i in range(b):
    lst = list(map(int,input().split()))[1:]
    result.append(set(lst))
    for j in lst:
        graph[j]= graph[j].union(set(lst)-{j})
temp = visited.copy()
for i in temp:
    bfs(graph,i,visited)
cnt = 0
for i in result:
    if i - visited ==i:
        cnt+=1
print(cnt)