import sys
n = int(input())
lst =[0,0,0]
lst_min = [0,0,0]
lst[0],lst[1],lst[2] = list(map(int,input().split()))
for i in range(3):
    lst_min[i] = lst[i]
for i in range(n-1):
    a,b,c = list(map(int,sys.stdin.readline().split()))
    x,y,z = lst[0],lst[1],lst[2]
    d,e,f = lst_min[0],lst_min[1],lst_min[2]
    lst[0]=max(x,y)+a
    lst[1]=max(max(x,y),z)+b
    lst[2]=max(y,z)+c
    lst_min[0]=min(d,e)+a
    lst_min[1]=min(min(d,e),f)+b
    lst_min[2]=min(e,f)+c

print(max(lst),min(lst_min))