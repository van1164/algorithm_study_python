import sys
from collections import deque
a, b = list(map(int,sys.stdin.readline().split()))
visited = {b}
i = 0
print("<"+str(b),end='')
i =b+b
while(len(visited)<a):
    print(i)
    if i%a in visited:
        while i%a in visited:
            i+=1
        if i%a ==0:
            visited.add(i%a)
            print(', '+str(a),end='')
        else:
            visited.add(i%a)
            print(', '+str(i%a),end='')
    else:
        if i%a ==0:
            visited.add(a)
            print(', '+str(a),end='')
        else:
            visited.add(i%a)
            print(', '+str(i%a),end='')
    i+=b    
        
print(">",end="")