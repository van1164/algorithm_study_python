from collections import deque
a,b = list(map(int,input().rstrip().split()))
def bfs(a,b):
    stack  = deque([a])
    visited = {a:0}
    while stack:
        n= stack.popleft()
        if n == b:
            print(visited[n])
            break
        else:
            for i in (n-1,n+1,n*2):
                if i not in visited and 0<=i<=100010:
                    stack.append(i)
                    visited[i] = visited[n]+1
bfs(a,b)