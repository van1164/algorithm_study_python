from collections import deque

string = input()
lst = deque()
for i in string:
    lst.append(i)
temp = deque()
for i in range(len(lst)):
    if lst[i]=='(':
        i+=1
        strr = lst[i]
        while(lst[i]!=')'):
            