import heapq
import sys
input = sys.stdin.readline

t = int(input())

lst = []
for i in range(t):
    a = int(input())
    heapq.heappush(lst,a)
if t ==1:
    print(0)
    exit()
count = 0
while len(lst)>1:
    first = heapq.heappop(lst)
    two = heapq.heappop(lst)
    if lst:
        count+=(first+two)
    heapq.heappush(lst,first+two)
    
print(count+heapq.heappop(lst))