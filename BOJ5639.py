import sys
sys.setrecursionlimit(10**6)

def reverse_preorder(graph,root,a):
    if root not in graph:
        graph[root]=[-1,-1]
    
    if root>a:
        if graph[root][0] !=-1:
            reverse_preorder(graph,graph[root][0],a)
        else:
            graph[root][0] = a
            graph[a] = [-1,-1]
    else:
        if graph[root][1] !=-1:
            reverse_preorder(graph,graph[root][1],a)
        else:
            graph[root][1] = a
            graph[a] = [-1,-1]
def postorder(graph,start,visited = []):
    if graph[start][0]==-1 and graph[start][1]==-1:
        visited.append(start)
    else:
        a,b = graph[start]
        if a != -1:
            postorder(graph,a,visited)
        if b != -1:
            postorder(graph,b,visited)
        visited.append(start)
    return visited
root = int(input())
graph = {root:[-1,-1]}   
while True:
    try:
        a= int(input())
        reverse_preorder(graph,root,a)
    except EOFError:
        break
for i in postorder(graph,root):
    print(i)