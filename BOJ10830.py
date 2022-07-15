import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)
def power(graph,n):
    if n ==1:
        return graph
    elif n%2 ==1:
        return multi(power(graph,n-1),graph)
    else:
        return power(multi(graph,graph),n//2)
    
    
def multi(graph1,graph2):
    n = len(graph1)
    m = len(graph2[0])
    mid = len(graph1[0])
    temp = [[0]*m for _ in range(n)]
    
    for i in range(m):
        for j in range(n):
            summ=0
            for k in range(mid):
                summ += graph2[k][i]* graph1[j][k]
            temp[j][i] = summ%1000
    return temp

n,m= list(map(int,input().split()))
graph = []
for _ in range(n):
    graph.append(list(map(int,input().split())))
result = power(graph,m)

for i in result:
    for j in i:
        print(j%1000,end =' ')
    print()