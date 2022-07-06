import sys

def right(graph,chung,R,C):
    temp = graph[chung][1]
    graph[chung][1] = 0
    for i in range(2,C+1):
        x = graph[chung][i]
        graph[chung][i] =temp
        temp = x
    return temp
def up(graph,start,end,R,C,tem):
    temp = graph[start-1][C]
    graph[start-1][C]=tem
    for i in range(start-2,end-1,-1):
        x = graph[i][C]
        graph[i][C]=temp
        temp = x
    return temp

def left(graph,R,C,tem):
    temp = graph[R][C-1]
    graph[R][C-1] = tem
    for i in range(C-2,-1,-1):
        x = graph[R][i]
        graph[R][i] =temp
        temp = x
    return temp

def down(graph,start,end,R,C,tem):
    temp = graph[start+1][C]
    graph[start+1][C]=tem
    for i in range(start+2,end+1):
        x = graph[i][C]
        graph[i][C]=temp
        temp = x
    return temp

def clean(graph,chung,R,C):
    temp = right(graph,chung-1,R,C)
    temp = up(graph,chung-1,0,R,C,temp)
    temp = left(graph,0,C,temp)
    down(graph,0,chung-1,R,0,temp)
    graph[chung-1][0] = -1
    temp = right(graph,chung,R,C)
    temp = down(graph,chung,R,R,C,temp)
    temp = left(graph,R,C,temp)
    up(graph,R,chung,R,0,temp)
    graph[chung][0] = -1
    

def dirty(graph,chung,R,C):
    temp_graph =[[0]*C for _ in range(R)]
    temp_graph[chung][0]=-1
    temp_graph[chung-1][0]=-1
    dx=[0,0,1,-1]
    dy = [1,-1,0,0]
    for i in range(R):
        for j in range(C):
            temp = graph[i][j]
            if temp ==-1:
                continue
            div = temp//5
            for k in range(4):
                x = i+dx[k]
                y = j +dy[k]
                if 0<=x<R and 0<=y<C and temp_graph[x][y]!=-1:
                    temp_graph[x][y]+=div
                    temp -=div
            temp_graph[i][j]+=temp
    return temp_graph


R,C,T = list(map(int,sys.stdin.readline().split()))
graph = []
chung = 0
for i in range(R):
    lst = list(map(int,sys.stdin.readline().split()))
    if lst[0] ==-1:
        chung= i
    graph.append(lst)
    
for i in range(T):
    graph = dirty(graph,chung,R,C)    
    clean(graph,chung,R-1,C-1)    
summ =0
for i in graph:
    summ+=sum(i)
print(summ+2)