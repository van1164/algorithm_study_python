from collections import deque
t = int(input())
for i in range(t):
    a,b = list(map(int,input().split()))
    visited = set()
    stack = deque([(a,'')])
    while stack:
        n = stack.popleft()
        d1 = n[0] // 1000
        d2 = n[0] // 100 - d1 * 10
        d3 = n[0] // 10 - d2 * 10 - d1 * 100
        d4 = n[0] - d3 * 10 - d2 * 100 - d1 * 1000
        if n[0] == b:
            print(n[1])
            break
        d=(n[0]*2)%10000
        s=n[0]-1 if n[0] else 9999
        l = d2 * 1000 + d3 * 100 + d4 * 10 + d1
        r = d4 * 1000 + d1 * 100 + d2 * 10 + d3
        if d not in visited:
            visited.add(d)
            stack.append((d,n[1]+'D'))
        if s not in visited:
            visited.add(s)
            stack.append((s,n[1]+'S'))
        if l not in visited:
            visited.add(l)
            stack.append((l,n[1]+'L'))
        if r not in visited:
            visited.add(r)
            stack.append((r,n[1]+'R'))