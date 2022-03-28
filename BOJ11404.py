def floyd(n,graph):
    for mid in range(n):
        for start in range(n):
            for end in range(n):
                if  graph[start][end] > graph[start][mid] + graph[mid][end]:
                    graph[start][end] = graph[start][mid] + graph[mid][end]

INF = 987654321
a= int(input())
b = int(input())
graph = []
for i in range(a):
    lst = [INF]*a
    lst[i] = 0
    graph.append(lst)
for i in range(b):
    x,y,z = list(map(int,input().split()))
    if graph[x-1][y-1] != INF:
        graph[x-1][y-1] = min(graph[x-1][y-1],z)
    else:
        graph[x-1][y-1] = z

floyd(a,graph)
for i in graph:
    for j in i:
        if j ==INF:
            print(0,end=' ')
        else:
            print(j,end=' ')
    print()