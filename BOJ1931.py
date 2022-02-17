def recursive(graph,start,n,lst={-1:0,0:0,1:0}):
    if n ==1:
        for k in range(start[0],start[0]+3):
            for l in range(start[1], start[1]+3):
                lst[int(graph[k][l])]+=1
        return lst
    flag =False
    for i in range(start[0],start[0]+3**n,3**(n-1) ):
        for j in range(start[1],start[1]+3**n, 3**(n-1)):
            statis = graph[i][j]
            for k in range(i,i+3**(n-1)):
                for l in range(j, j+3**(n-1)):
                    if graph[k][l] != statis:
                        flag = True
                        recursive(graph,(i,j),n-1,lst)
                        break
                if flag:
                    break
            if not flag:        
                lst[int(statis)]+=1
            flag =False
    return lst

a = int(input())
lst = []
for i in range(a):
    lst.append(list(map(int,input().split())))
n =0
for i in range(a):
    if a==3**i:
        n =i
statis = lst[0][0]
for i in lst:
    for j in i:
        if j!=statis:
            sett =recursive(lst,(0,0),n)
            for k in sett:
                print(sett[k])
            exit()
for i in (-1,0,1):
    if i ==statis:
        print(1)
    else:
        print(0)
                
                
            