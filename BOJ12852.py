import heapq
N =int(input())
dic =dict()
stack =[(0,N,[])]

while stack:
    time,n,lst =heapq.heappop(stack)
    if n ==1:
        print(time)
        for i in lst:
            print(i,end=' ')
        print(1)
        break
    if n%3 ==0:
        heapq.heappush(stack,(time+1,n//3,lst+[n]))
    if n%2 ==0:
        heapq.heappush(stack,(time+1,n//2,lst+[n]))
    heapq.heappush(stack,(time+1,n-1,lst+[n]))
    