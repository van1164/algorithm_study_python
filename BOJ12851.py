from collections import deque
a,b = list(map(int,input().split()))
stack = deque([(a,0)])
minn =  10000000000
cnt =0
while stack:
    n = stack.popleft()
    if n[1]>minn or n[0]<=0 or n[0]>100000:
        continue
    if n[0] == b:
        minn = n[1]
        cnt+=1
    x = n[0]+1
    y = n[0]-1
    z = n[0]*2
    t =n[1]+1
    tmp = set()
    for i in (x,y,z):
        stack.append((i,t))
            
print(minn)
print(cnt)
    