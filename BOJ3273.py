import sys
input = sys.stdin.readline

t = int(input())
lst = sorted(list(map(int,input().split(' '))))
title = int(input())
count =0
for i in range(t):
    findig = title-lst[i]
    start = i
    end = t-1
    while start<=end:
        mid = (end +start)//2
        if lst[mid]<findig:
            start = mid+1
        elif lst[mid]>findig:
            end = mid-1
        else:
            if mid != i:
                count+=1
            break
        
print(count)