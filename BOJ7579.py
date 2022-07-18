N,M = list(map(int,input().split()))
graph = list(map(int,input().split()))
lst= list(map(int,input().split()))
dic = dict()
visit = []
length = sum(lst)+1
for i in range(N):
    visit.append((graph[i],lst[i]))
graph= [[0]*(length+1) for _ in range(N+1)]
k =1
for memory,cost in visit:
    for i in range(0,cost):
        graph[k][i] = graph[k-1][i]
    for i in range(cost,length):
        graph[k][i] = max(graph[k-1][i],graph[k-1][i-cost] + memory)
    k+=1
for i in range(length):
    if graph[-1][i]>=M:
        print(i)
        break