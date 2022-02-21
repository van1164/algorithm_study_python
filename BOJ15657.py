def back_track(n,graph,lst,count,tmp=0,arr =[],start=0):
    if tmp==count:
        lst.append(arr)
    else:
        for i in range(start,n):
            back_track(n,graph,lst,count,tmp+1,arr+[graph[i]],i)
    return lst
    

a,b = list(map(int,input().split()))
graph = sorted(list(map(int,input().split())))
lst = []
for i in sorted(back_track(a,graph,lst,b)):
    for j in i:
        print(j,end=' ')
    print()
