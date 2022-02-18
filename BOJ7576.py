import sys
from collections import deque

def bfs(graph,end,que):
    visited= set()
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    while que:
        n  = que.popleft()
        x  =graph[n[1]][n[0]]
        for i in range(4):
            a =n[0] + dx[i]
            b =n[1] + dy[i]
            if (a,b) not in visited:
                visited.add((a,b))
                if(0<=a<end[0] and 0<=b<end[1]):
                    if graph[b][a]==-1:
                        continue
                    que.append((a,b))
                    if  graph[b][a]==0:
                        graph[b][a] = x +1
                    elif graph[b][a] > x+1:
                        graph[b][a] = x+1
                    else:
                        continue
    
    
    
    
def solution():
    a,b = list(map(int,sys.stdin.readline().rstrip().split()))
    lst = []
    for j in range(b):
        lst.append(list(map(int,sys.stdin.readline().rstrip().split())))           
    que = deque([])
    for j in range(b):
        for k in range(a):
            if lst[j][k] == 1:
                que.append((k,j))
    bfs(lst,(a,b),que)
            
    maxx = 0

    for i in lst:
        for j in i:
            if j>maxx:
                maxx = j
            elif j == 0:
                print(-1)
                return 0
            
    print(maxx-1)


        
    

solution()