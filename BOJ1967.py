import sys
sys.setrecursionlimit(10 ** 9)
def dfs_distance(dic,start,w,visited):
    
    for i,a in dic[str(start)]:
        if visited[i]==-1:
            visited[i]=w+a
            dfs_distance(dic,i,w+a,visited)


a = int(input())
dic = dict()
maxx =0
for j in range(1,a+1):
    dic[str(j)] = list()
for i in range(a-1):
    lst = list(map(int,sys.stdin.readline().split()))
    dic[str(lst[0])].append((lst[1],lst[2]))
    dic[str(lst[1])].append((lst[0],lst[2]))
visited = [-1]*(a+1)
visited[1] =0
dfs_distance(dic,1,0,visited)
x = visited.index(max(visited))
visited = [-1]*(a+1)
visited[x]=0
dfs_distance(dic,x,0,visited)
maxx = max(visited)
print(maxx)
