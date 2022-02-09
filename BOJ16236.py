import sys
from collections import deque
import heapq

def bfs(graph,start,end,size):
    visited = set()
    stack = deque([start])
    dx = [0,-1,1,0]
    dy = [-1,0,0,1]
    ate = 0
    moving =0
    while(True):
        tmp = []
        minn = 100
        while stack:
            n = stack.popleft()
            visited.add((n[0],n[1]))
            if  n[2]+1>minn:
                stack = []
                break
            for i in range(4):
                x = n[0] +dx[i]
                y = n[1] +dy[i]
                if  (x,y) not in visited and x<end and y <end and x>=0 and y>=0 and graph[y][x]<=size and n[2]+1<=minn:
                    if graph[y][x] <size and graph[y][x]!=0 :
                        heapq.heappush(tmp,((n[2]+1),y,x))
                        minn = n[2]+1
                        break
                    else:
                        stack.append((x,y,n[2]+1))
        if not tmp and not stack:
            break
        elif tmp:
            start = heapq.heappop(tmp)
            moving+=start[0]
            start = (start[2],start[1],0)
            stack=deque([start])
            ate+=1
            if ate ==size:
                size+=1
                ate =0
            visited = set()
            graph[start[1]][start[0]] = 0
            tmp = []
        else:
            break

    return moving
            
        
    


graph = []
a= int(sys.stdin.readline().rstrip())
for i in range(a):
    lst = list(map(int,sys.stdin.readline().rstrip().split()))
    graph.append(lst)
start =tuple()
for i in range(a):
    for j in range(a):
        if graph[j][i] == 9:
            graph[j][i] = 0
            start = (i,j,0)
print(bfs(graph,start,a,2))