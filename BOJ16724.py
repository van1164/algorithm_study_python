import sys
from collections import deque


def bfs(graph,start,visited):
    stack = deque([start])
    print(start)
    while stack:
        x,y = stack.popleft()
        if graph[x][y] == 'U':
            next_x,next_y = x-1,y
        elif graph[x][y] == 'D':
            next_x, next_y = x+1, y
        elif graph[x][y] == 'R':
            next_x, next_y = x,y+1
        else:
            next_x, next_y = x,y-1
        
        if not visited[next_x][next_y]:
            visited[next_x][next_y] =  True
            stack.append((next_x,next_y))
                


N,M = list(map(int,sys.stdin.readline().split()))

graph = []
for i in range(N):
    graph.append(sys.stdin.readline().rstrip())

visited = [[False]*M for _ in range(N)]


cnt=0
for i in range(N):
    for j in range(M):
        if not visited[i][j]:
            visited[i][j] = True
            bfs(graph,(i,j),visited)
            cnt+=1

print(cnt)