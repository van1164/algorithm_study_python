lst = list(map(int,input().split()))
graph = [[1000000]*5 for _ in range(5)]
energy = [[0,2,2,2,2],[0,1,3,4,3],[0,3,1,3,4],[0,4,3,1,3,],[0,3,4,3,1]]
graph[0][0]=0
if len(lst) ==1:
    print(0)
    exit()
for num in lst:
    if num == 0:
        break
    temp_graph = [[1000000]*5 for _ in range(5)]
    for i in range(5):
        for j in range(5):
            if graph[i][j]!=-1:
                if i == num or j ==num:
                    temp_graph[i][j] = min(temp_graph[i][j],graph[i][j]+1)
                    continue
                temp_graph[num][j] = min(temp_graph[num][j],graph[i][j] +energy[i][num])
                temp_graph[i][num] = min(temp_graph[i][num],graph[i][j] +energy[j][num])

    graph = temp_graph


                    
finding = lst[-2]
minn = 10000000000000000
for i in range(5):
    if graph[finding][i]!=-1:
        minn = min(minn,graph[finding][i])
    if graph[i][finding]!=-1:
        minn = min(minn,graph[i][finding])
print(minn)