from collections import deque

def bfs(graph,x,y):
    for i in range(1,y):
        for j in range(1,x):
            if graph[i][j] == -1:
                graph[i][j] = 0
            else:
                graph[i][j] = (graph[i-1][j] + graph[i][j-1])%1000000007
    
    #stack =deque([((0,0),xCount,yCount)])
    
    # while stack:
    #     (x,y),countX,countY = stack.popleft()
    #     graph[y][x]= (graph[y][x]+1)%1000000007
    #     if(countX>0 and graph[y][x+1] !=-1):
    #         stack.append(((x+1,y),countX-1,countY))
    #     if(countY>0 and graph[y+1][x] !=-1):
    #         stack.append(((x,y+1),countX,countY-1))
    #print(graph)
    return graph[-1][-1]%1000000007

def solution(m, n, puddles):
    graph = [[0]*m for _ in range(n)]
    for x,y in puddles:
        graph[y-1][x-1] = -1
    firstInput = 1
    for i in range(m):
        if graph[0][i] == -1:
            firstInput =0
        graph[0][i] =firstInput
    firstInput = 1
    for j in range(n):
        if graph[j][0] == -1:
            firstInput = 0
        graph[j][0] = firstInput
        
    #print(graph)
    answer = bfs(graph,m,n)
    return answer