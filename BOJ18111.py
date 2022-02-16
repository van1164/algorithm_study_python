def find_max(graph):
    maxx = 0
    idx = 0
    for i in range(len(graph)):
        for j in range(len(graph[i])):
            if graph[i][j]>maxx:
                maxx = graph[i][j]
                idx = (i,j)
    return [maxx,idx]

def found(graph,maxx):
    cnt = 0
    for i in range(len(graph)):
        for j in range(len(graph[i])):
            cnt+= maxx -graph[i][j]
    return cnt
a,b,inven = list(map(int,input().split()))
graph = []
for i in range(a):
    graph.append(list(map(int,input().split())))
cnt = 0
minn = 100000000
item = 4000
while True:
    maxx,idx = find_max(graph)
    founding = found(graph,maxx)
    if cnt>minn:
        print(minn,item)
        break
    if founding == 0 :
        if cnt<minn:
            print(cnt,maxx)
        else:
            print(minn,item)
        break
    if founding>inven:
        graph[idx[0]][idx[1]]-=1
        inven+=1
        cnt+=2
    else:
        if founding+cnt<minn:
            minn = founding+cnt
            item = maxx
            cnt+=2
            graph[idx[0]][idx[1]]-=1