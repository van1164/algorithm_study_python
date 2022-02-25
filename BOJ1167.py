from collections import deque
def dfs(graph,start,visited = set(),weight = [0], k =0):
    weight[0] = max(k,weight[0])
    print(start,weight[0],k)
    for i in graph[start]-visited:
        visited.add(i)
        dfs(graph,i[0],visited,weight,k+i[1])
    
    return weight



t=int(input())
dic = dict()
for i in range(1,t+1):
    dic[i]=set()
for i in range(t):
    lst = list(map(int,input().split()))
    k = lst[0]
    for j in range(1,len(lst)-1,2):
        dic[k].add((lst[j],lst[j+1]))
result = {}
for i in range(1,t+1):
    result[i]= dfs(dic,i,set(),[0])
    print(result[i])
    print("----------------------------------------")

print(result)
