import sys
a = int(input())
lst =[1000]*(a+1)
lst[a] = 0
for i in range(a,-1,-1):
    if lst[i-1]>lst[i]+1:
        lst[i-1] = lst[i]+1
    if i%2 ==0 and lst[i//2]>lst[i]+1:
        lst[i//2] = lst[i]+1
    if i%3 ==0 and lst[i//3]>lst[i]+1:
        lst[i//3] = lst[i]+1
print(lst[1])