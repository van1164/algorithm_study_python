import sys
sys.setrecursionlimit(10**9)
def dfs(lst,des,N,start,visited):
    if visited[start]:
        return
    for i in des[start]:
        dfs(lst,des,N,i,visited)
    maxx = 0
    for i in des[start]:
        if maxx < lst[i]:
            maxx =lst [i]
    lst[start]+=maxx
    visited[start]=True
                


tc = int(sys.stdin.readline())
for i in range(tc):
    N,M = list(map(int,sys.stdin.readline().split()))
    lst =[-1]+ list(map(int,sys.stdin.readline().split()))
    des =[[] for _ in range(N+1)]
    for _ in range(M):
        a,b  = list(map(int,sys.stdin.readline().split()))
        des[b].append(a)
    start = int(sys.stdin.readline())
    visited = [False]*(N+1)
    dfs(lst,des,N,start,visited)
    print(lst[start])