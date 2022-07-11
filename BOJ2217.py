import sys

N = int(sys.stdin.readline())
lst =[]
for _ in range(N):
    lst.append(int(sys.stdin.readline()))
lst.sort()
cnt=1
maxx =0
for i in range(N-1,-1,-1):
    a = cnt*lst[i]
    if maxx<a:
        maxx =a
    cnt+=1
print(maxx)