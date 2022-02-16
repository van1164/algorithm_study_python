from collections import deque
def bfs_real(graph,start,end):
    character = graph[start[0]][start[1]]
    graph[start[0]][start[1]] = 'X'
    visited = {start}
    stack = deque([start])
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    while stack:
        n = stack.popleft()
        for i in range(4):
            x = n[0] +dx[i]
            y= n[1]+dy[i]
            if 0<=x<end and 0<=y<end and (x,y) not in visited and graph[x][y]==character:
                visited.add((x,y))
                stack.append((x,y))
                graph[x][y] = 'X'
    return len(visited)


a = int(input())
lst = []
for i in range(a):
    lst.append(list(input()))
lst_fake = []
flag = True
for i in lst:
    for j in i:
        if j != 'G':
            flag =False
            break
    if flag == False:
        break
if flag:
    print(1,1)
    exit()

for i in lst:
    tmp = []
    for j in i:
        if j== "G":
            tmp.append('R')
        else:
            tmp.append(j)
    lst_fake.append(tmp)
cnt_green = 0
while True:
    boo = True
    for i in range(a):
        for j in range(a):
            if lst_fake[i][j]=='R' or lst_fake[i][j]=='B':
                cnt_green+=1
                bfs_real(lst_fake,(i,j),a)
                boo=False

    if boo:
        break    
cnt_red_blue = 0
while True:
    boo = True
    for i in range(a):
        for j in range(a):
            if lst[i][j]=='R' or lst[i][j]=='B' or lst[i][j]=='G':
                cnt_red_blue+=1
                bfs_real(lst,(i,j),a)
                boo=False
    if boo:
        break
print(str(cnt_red_blue)+ ' '+str(cnt_green))