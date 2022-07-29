import heapq
import sys

N,M = list(map(int,sys.stdin.readline().split()))
muge = []
gabang = []
for i in range(N):
    
    a,b = list(map(int,sys.stdin.readline().split()))
    
    heapq.heappush(muge,(-b,a))
    
summ = 0
for j in range(M):
    a = int(sys.stdin.readline())
    heapq.heappush(gabang,-a)

mid = 100000000000000
big = []
while muge and (gabang or big):
    don,mu = heapq.heappop(muge)
    
    if mu>=mid:
        if big and -big[0]<mu:
            continue
    else:
        if gabang and -gabang[0]<mu:
            continue
    temp = []
    ga = 10000000000
    if mu<mid and gabang:
        while ga>= mu and gabang:
            ga = -heapq.heappop(gabang)
            temp.append(-ga)
        if gabang:
            heapq.heappush(gabang,temp.pop())
        temp.pop()
        summ -=don
        while temp:
            heapq.heappush(big,temp.pop())
    else:
        while ga>= mu and big:
            ga = -heapq.heappop(big)
            temp.append(-ga)
        if big:
            heapq.heappush(gabang,temp.pop())
        temp.pop()
        summ -=don
        while big:
            heapq.heappush(gabang,big.pop())
        while temp:
            heapq.heappush(big,temp.pop())
    mid = mu
        
print(summ)