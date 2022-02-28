import sys
a,b = list(map(int,sys.stdin.readline().split()))
last = 0
graph = [[0]*a]
for i in range(a):
    lst = list(map(int, sys.stdin.readline().split()))
    tmp = []
    for j in range(a):
        tmp.append(graph[i][j]+lst[j])
    graph.append(tmp)
for i in range(b):
    q,w,e,r = list(map(int,sys.stdin.readline().split()))
    summ = 0
    for j in range(w,r+1):
        summ +=graph[e][j-1]-graph[q-1][j-1]
    sys.stdout.write(str(summ)+'\n')