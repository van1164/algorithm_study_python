import sys
sys.setrecursionlimit(10**9)
def is_pell(graph,lst,start,end):
    if start>end:
        return 1
    if graph[start][end]==-1:
        if lst[start] == lst[end]:
            if is_pell(graph,lst,start+1,end-1):
                graph[start][end]=1
                return 1
            else:
                graph[start][end]=0
                return 0
        else:
            graph[start][end]=0
            return 0
    else:
        return graph[start][end]
        
N= int(sys.stdin.readline())
lst = list(map(int,sys.stdin.readline().split()))
graph = [[-1]*(N) for _ in range(N)]

for i in range(N):
    graph[i][i]=1
    
    

for k in range(N):
    graph[k][k]=1
    
tc= int(sys.stdin.readline())
for i in range(tc):
    N,M = list(map(int,sys.stdin.readline().split()))
    start =N-1
    end = M-1
    print(is_pell(graph,lst,start,end))
    