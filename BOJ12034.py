import sys
tc = int(sys.stdin.readline())
for i in range(tc):
    N = int(sys.stdin.readline())
    lst = list(map(int,sys.stdin.readline().split()))
    for k in range(len(lst)):
        if lst[k]==-1:
            continue
        num = lst[k]*(4/3)
        temp = k
        temp+1
        while(True):
            if lst[temp]==num:
                lst[temp] = -1
                break
            else:
                temp+=1

    print("Case #"+str(i+1)+": ",end='')
    lst.sort()
    for t in lst:
        if t==-1:continue
        print(t,end=' ')
    print()