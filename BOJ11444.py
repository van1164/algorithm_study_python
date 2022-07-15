global graph
graph = list()

def back(lst,N,M,visited = [],cnt=0):
    global graph
    if M==cnt:
        graph.append(visited)
        return
    for i in range(0,N):
        if i in visited:
            continue
        back(lst,N,M,visited+[i],cnt+1)
    

N,M = list(map(int,input().split()))
lst = list(map(int,input().split()))
dup = dict()
lst.sort()
prev = -1
for i in lst:
    if prev == i:
        if i in dup:
            dup[i]+=1
        else:
            dup[i]=1
    else:
        prev = i
    
print(dup)


back(lst,N,M)
prev = []
for i in graph:
    if prev ==i:
        continue
    else:
        for k in i:
            print(lst[k],end=' ')
        print()
        prev = i

