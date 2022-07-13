import sys
sys.setrecursionlimit(10**9)
global cnt
cnt = 0

def poss(row):
    for i in range(row):
        if (graph[i] ==graph[row]) or ((row-i) == abs(graph[row]-graph[i])) :
            return False
    return True

def dfs(row,N):
    global cnt
    if row ==N:
        cnt+=1
        return
    
    for col in range(N):
        graph[row] = col
        
        if poss(row):
            dfs(row+1,N)
        
    

N= int(input())
graph = [-1]*N
dfs(0,N)
print(cnt)