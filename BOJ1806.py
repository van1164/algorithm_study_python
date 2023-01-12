from collections import deque
from math import log2,ceil

N,M = list(map(int, input().split()))
lst =  list(map(int, input().split()))
x = int(ceil(log2(N)))
result = [0]*(pow(2,x+1))
end = len(result)
start = pow(2,x)

k =0
for i in range(start,start+len(lst)):
    result[i] = lst[k]
    k+=1

for i in range(len(result)-1,0,-2):
    result[i//2]=result[i]+result[i-1]


for i in range(len(result)-1,0,-1):
    if result[i]>=M:
        print(int(log2(len(result))) -int(log2(i)))
        exit()
