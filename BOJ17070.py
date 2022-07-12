from collections import deque
import sys
#state  가로 :0 대각선 :1 세로 :2


def bfs(graph,start,state,end,N):
    stack = deque([(start,state)])
    cnt = 0
    while stack:
        tup,state = stack.popleft()
        if tup == end:
            cnt+=1
            continue
        a,b =tup
        if state ==0:
            if b+1<N and not graph[a][b+1]:
                stack.append(((a,b+1),0))
            if a+1<N and b+1<N:
                if not( graph[a+1][b] or graph[a][b+1] or graph[a+1][b+1]):
                    stack.append(((a+1,b+1),1))
            
        elif state ==1:
            if a+1<N and not graph[a+1][b]:
                stack.append(((a+1,b),2))
            if  a+1<N and b+1<N:
                if not( graph[a+1][b] or graph[a][b+1] or graph[a+1][b+1]):
                    stack.append(((a+1,b+1),1))
            if b+1<N and not graph[a][b+1]:
                stack.append(((a,b+1),0))
        else:
            if a+1<N and b+1<N:
                if not( graph[a+1][b] or graph[a][b+1] or graph[a+1][b+1]):
                    stack.append(((a+1,b+1),1))
            if a+1<N and not graph[a+1][b]:
                stack.append(((a+1,b),2))     
                
    return cnt



def dfs(graph,start,state,end,N,result):
    if start ==end:
        result[0]+=1
        return
    a,b = start
    if state ==0:
        if b+1<N and not graph[a][b+1]:
            dfs(graph,(a,b+1),0,end,N,result)
        if a+1<N and b+1<N:
            if not( graph[a+1][b] or graph[a][b+1] or graph[a+1][b+1]):
                dfs(graph,(a+1,b+1),1,end,N,result)
        
    elif state ==1:
        if a+1<N and not graph[a+1][b]:
            dfs(graph,(a+1,b),2,end,N,result)
        if  a+1<N and b+1<N:
            if not( graph[a+1][b] or graph[a][b+1] or graph[a+1][b+1]):
                dfs(graph,(a+1,b+1),1,end,N,result)
        if b+1<N and not graph[a][b+1]:
            dfs(graph,(a,b+1),0,end,N,result)
    else:
        if a+1<N and b+1<N:
            if not( graph[a+1][b] or graph[a][b+1] or graph[a+1][b+1]):
                dfs(graph,(a+1,b+1),1,end,N,result)
        if a+1<N and not graph[a+1][b]:
            dfs(graph,(a+1,b),2,end,N,result)     


def dynamic(graph,one,two,three,start,end,N):
    a,b = start
    if one[a][b]:
        if b+1<N and not graph[a][b+1]:
            one[a][b+1]+=one[a][b]
        if a+1<N and b+1<N:
            if not( graph[a+1][b] or graph[a][b+1] or graph[a+1][b+1]):
                two[a+1][b+1]+=one[a][b]
    if two[a][b]:
        if a+1<N and not graph[a+1][b]:
            three[a+1][b]+=two[a][b]
        if  a+1<N and b+1<N:
            if not( graph[a+1][b] or graph[a][b+1] or graph[a+1][b+1]):
                two[a+1][b+1]+=two[a][b]
        if b+1<N and not graph[a][b+1]:
            one[a][b+1]+=two[a][b]
    if three[a][b]:
        if a+1<N and b+1<N:
            if not( graph[a+1][b] or graph[a][b+1] or graph[a+1][b+1]):
                two[a+1][b+1]+=three[a][b]
        if a+1<N and not graph[a+1][b]:
            three[a+1][b]+=three[a][b]
    

N = int(sys.stdin.readline())
graph = []

for _ in range(N):
    graph.append(list(map(int,sys.stdin.readline().split())))
result =[0]
#dfs(graph,(0,1),0,(N-1,N-1),N,result)
#print(result[0])
#print(bfs(graph,(0,1),0,(N-1,N-1),N))
one = [[0]*N for _ in range(N)]
two = [[0]*N for _ in range(N)]
three = [[0]*N for _ in range(N)]
one[0][1]=1
for i in range(N):
    for j in range(N):
        if i==0 and j==0:
            continue
        dynamic(graph,one,two,three,(j,i),(N-1,N-1),N)
        
print(one[N-1][N-1]+two[N-1][N-1]+three[N-1][N-1])