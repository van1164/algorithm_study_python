def back_track(n,lst,count,tmp=0,arr =[],start =1):
    if tmp==count:
        lst.append(arr)
    elif count-tmp>n-start+1:
        pass
    else:
        for i in range(start,n+1):
            back_track(n,lst,count,tmp+1,arr+[i],i+1)
    
    return lst
    

a,b = list(map(int,input().split()))
lst = []
for i in back_track(a,lst,b):
    for j in i:
        print(j,end=' ')
    print()
