from collections import deque
def bfs(graph,start,end):
    stack = deque([start])
    True_visited = {(start[0],start[1])}
    False_visited = {(start[0],start[1])}
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    while stack:
        n = stack.popleft()
        if (n[0],n[1]) == (end[0]-1,end[1]-1):
            print(n[3])
            return 0
        for i in range(4):
            x=n[0]+dx[i]
            y=n[1]+dy[i]
            if n [2]==False:
                if (x,y) not in False_visited and 0<=x<end[0] and 0<=y<end[1]:
                    if graph[x][y] =='1':   
                        False_visited.add((x,y))
                        stack.append((x,y,True,n[3]+1))
                    else:
                        False_visited.add((x,y))
                        stack.append((x,y,n[2],n[3]+1))
            else:
                if (x,y) not in True_visited and(x,y) not in False_visited and 0<=x<end[0] and 0<=y<end[1]:
                    if graph[x][y] =='1':   
                        pass
                    else:
                        True_visited.add((x,y))
                        stack.append((x,y,n[2],n[3]+1))
    return 1
        

a,b = list(map(int,input().split()))
graph = []
for i in range(a):
    graph.append(list(input()))
if bfs(graph,(0,0,False,1),(a,b)):
    print(-1)