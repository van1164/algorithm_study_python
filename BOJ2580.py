
graph = []
zeroList = []

def printList(graph):
    for row in graph:
        for col in row:
            print(col,end=" ")
        print()

def findWhere(x,y):
    if(y<3):
        yRange = range(0,3)
    elif(y<6):
        yRange = range(3,6)
    else:
        yRange = range(6,9)

    if(x<3):
        xRange = range(0,3)
    elif(x<6):
        xRange = range(3,6)
    else:
        xRange = range(6,9)

    return (xRange,yRange)

def checkX(i,x):
    if i in graph[x]:
        return False
    else: return True




def dfs(idx):
    if(len(zeroList)==idx):
        return (True, graph)
    x,y = zeroList[idx]
    yList = [graph[j][y] for j in range(9)]
    rangeX,rangeY = findWhere(x,y)
    tempList = []
    for i in rangeX:
        for j in rangeY:
            tempList.append(graph[i][j])

    itemList = []
    for i in range(1,10):
        if (i  not in graph[x]) and (i not in yList) and (i not in tempList):
            itemList.append(i)
    for i in itemList:
        graph[x][y] = i
        finish, result = dfs(idx+1)

        if finish:
            return (finish, result)
        else:
            graph[x][y] = 0
    return (False, graph)    



for i in range(9):
    line = list(map(int,input().split(" ")))
    graph.append(line)
    for j in range(9):
        if(line[j]==0):
            zeroList.append((i,j))
x,a = dfs(0)
printList(a)