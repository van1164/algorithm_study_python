global graph
graph = list()

def back(lst,N,M,start=0,visited = [],cnt=0):
    global graph
    if M==cnt:
        graph.append(visited)
        return
    for i in range(start,N):
        back(lst,N,M,i,visited+[lst[i]],cnt+1)
    

N,M = list(map(int,input().split()))
lst = list(map(int,input().split()))
lst = list(set(lst))
lst.sort()
N = len(lst)
back(lst,N,M)
prev = []
for i in graph:
    if prev ==i:
        continue
    else:
        for k in i:
            print(k,end=' ')
        print()
        prev = i

