import sys
from collections import deque

def bfs(graph,real_end,end,que):
    visited= set()
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    d2y = [-end[1],end[1]]
    while que:
        n  = que.popleft()
        x  =graph[n[1]][n[0]]
        for i in range(4):
            a =n[0] + dx[i]
            b =n[1] + dy[i]
            if(0<=a<end[0] and n[2]*end[1]<=b<n[2]*end[1]+end[1]):
                if (a,b) not in visited:
                    visited.add((a,b))
                    if graph[b][a]==-1:
                        continue
                    que.append((a,b,n[2]))
                    if  graph[b][a]==0:
                        graph[b][a] = x +1
                    elif graph[b][a] > x+1:
                        graph[b][a] = x+1
                    else:
                        continue
        for i in range(2):
            a= n[0]
            b=n[1]+d2y[i]
            if(0<=a<end[0] and 0<=b<real_end):
                if (a,b) not in visited:
                    visited.add((a,b))
                    if graph[b][a]==-1:
                        continue
                    que.append((a,b,int(b/end[1])))
                    if  graph[b][a]==0:
                        graph[b][a] = x +1
                    elif graph[b][a] > x+1:
                        graph[b][a] = x+1
                    else:
                        continue
    

    
def solution():
    a,b,c = list(map(int,sys.stdin.readline().rstrip().split()))
    lst = []
    for j in range(b*c):
        lst.append(list(map(int,sys.stdin.readline().rstrip().split())))           
    que = deque([])
    for j in range(b*c):
        for k in range(a):
            if lst[j][k] == 1:
                que.append((k,j,int(j/b)))
    bfs(lst,c*b,(a,b),que)
            
    maxx = 0
    for i in lst:
        for j in i:
            if j>maxx:
                maxx = j
            elif j == 0:
                print(-1)
                exit()
    print(maxx-1)
    

        
    

solution()