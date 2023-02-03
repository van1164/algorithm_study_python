import heapq
import sys
input = sys.stdin.readline

t = int(input())
lst = []
for i in range(t):
    x,y = list(map(int,input().split()))
    lst.append((x,y))
heap=[]
for i in range(len(lst)):
    x,y = lst[i]
    count=0
    for j in range(len(lst)):
        if i == j :
            continue
        new_x, new_y = lst[j]
        if(new_x<x and new_y >y) or (new_x>x and new_y<y):
            count+=1
    heapq.heappush(heap,(-count,(x,y)))
result = 0

while heap:    
    print(heap)
    count, (x,y) = heapq.heappop(heap)
    if count ==0:
        break
    else:
        num =len(heap)
        new_heap =[]
        for j in range(num):
            new_count,(new_x,new_y) = heapq.heappop(heap)
            if(new_x<x and new_y >y) or (new_x>x and new_y<y):
                new_count+=1
            heapq.heappush(new_heap,(new_count,(new_x,new_y)))
        heap =new_heap
        result +=1

print(result)