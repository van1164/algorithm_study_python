from collections import deque

def bfs(graph,start,end,visited_now):
    stack = deque([start])
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    maxx = 0
    while stack:
        n = stack.popleft()
        if n[3] == 4 and n[4]<=5:
            if maxx<n[2]:
                maxx = n[2]
            continue
        elif n[3] >4 or n[4]>5 :
            break
        for i in range(4):
            x = n[0]+dx[i]
            y = n[1] + dy[i]
            if 0<=x<end[0] and 0<=y<end[1]and (x,y) not in visited_now:
                if (x,y) in n[5]:
                    stack.append((x,y,n[2],n[3],n[4]+1,n[5]))
                else:
                    stack.append((x,y,n[2]+graph[x][y],n[3]+1,n[4]+1,n[5].union({(x,y)})))
    return maxx


a,b = list(map(int,input().rstrip().split()))
lst =[]
for i in range(a):
    lst.append(list(map(int,input().rstrip().split())))
visited = set()
maxx = 0
for i in range(a):
    for j in range(b):
        tmp = bfs(lst,(i,j,lst[i][j],1,1,{(i,j)}),(a,b),visited)
        visited.add((i,j))
        if tmp >maxx:
            maxx = tmp
print(maxx)