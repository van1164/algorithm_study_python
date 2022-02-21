from collections import deque
def bfs(start,end):
    stack = deque([start])
    
    while stack:
        n = stack.popleft()
        if n[0]== end:
            if n[1]!=0:
                return n[1]+1
        a = int(str(n[0])+'1')
        b = n[0]*2
        if a<=end:
            stack.append((a,n[1]+1))
        if b<=end:
            stack.append((b,n[1]+1))
    return -1


a,b = list(map(int,input().split()))
print(bfs((a,0),b))