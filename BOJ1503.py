
def finding(n,visited,cnt=0,current =1, minn =[100000000]):
    if current >minn[0]:
        return -1
    if cnt==3:
        if abs(n-current)<minn[0]:
            minn[0]= abs(n-current)
            return minn[0]
    i = 1
    while True:
        if i in visited:
            i+=1
            continue
        if finding(n,visited,cnt+1,current*i,minn)==-1:
            break
        i+=1
    return minn[0]


a,b = list(map(int,input().split()))
if b!=0:
    visited =set(map(int,input().split()))
else:
    visited = set()
print(finding(a,visited))
