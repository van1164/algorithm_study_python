
from collections import deque

N = int(input())
temp = list(map(int,input().split()))
minn = 10000000000000000000000
start =0
end = N-1
while start<end:
    if minn> abs(temp[start]+temp[end]):
        gwal = (temp[start],temp[end])
        minn = abs(temp[start]+temp[end])
    if temp[start]+temp[end]<0:
        start+=1
    else:
        end -=1

print(gwal[0],gwal[1])