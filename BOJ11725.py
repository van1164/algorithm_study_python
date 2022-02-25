from collections import deque
def bfs(graph,start):
    stack = deque([start])
    visited = {start}
    result = dict()
    while stack:
        n = stack.popleft()
        visited.add(n)
        for i in graph[n]:
            if i not in visited:
                visited.add(i)
                result[i] = n
                stack.append(i)
    return result



t=int(input())
dic = dict()
for i in range(1,t+1):
    dic[i]=set()
for i in range(t-1):
    a,b = list(map(int,input().split()))
    dic[a].add(b)
    dic[b].add(a)
lst  = bfs(dic,1)
for i in range(2,t+1):
    print(lst[i])    
