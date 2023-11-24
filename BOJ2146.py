from collections import deque
n = int(input())
graph = []
for i in range(n):
    graph.append(list(map(int,input().split(" "))))


dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs():
    stack = deque([0,[]])

    for x,y in bridgeList:
        graph[x][y] =1

    for i in range(4):
        x= bridgeList[-1][0] +dx[i]
        y= bridgeList[-1][1] + dy[i]





    for x,y in bridgeList:
        graph[x][y] = 0