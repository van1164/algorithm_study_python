def back_track(graph,lst,count,tmp=0,arr =[]):
    if tmp==count:
        lst.append(arr)
    else:
        for i in graph:
            back_track(graph-{i},lst,count,tmp+1,arr+[i])
    return lst
    

a,b = list(map(int,input().split()))
graph = set(map(int,input().split()))
lst = []
for i in sorted(back_track(graph,lst,b)):
    for j in i:
        print(j,end=' ')
    print()
