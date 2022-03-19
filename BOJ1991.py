from collections import deque
def preorder(graph,start,visited = []):
    visited.append(start)
    for i in graph[start]:
        if i not in visited and i != '.':
            preorder(graph,i,visited)
    return visited   

def inorder(graph,start,visited = []):
    if graph[start][0]=='.' and graph[start][1]=='.':
        visited.append(start)
    else:

        a,b = graph[start]
        if a != '.':
            inorder(graph,a,visited)
            visited.append(start)
        if b != '.':
            if start not in visited:
                visited.append(start)
            inorder(graph,b,visited)
            
    return visited
    
def postorder(graph,start,visited = []):
    if graph[start][0]=='.' and graph[start][1]=='.':
        visited.append(start)
    else:

        a,b = graph[start]
        if a != '.':
            postorder(graph,a,visited)
        if b != '.':
            postorder(graph,b,visited)
        visited.append(start)
            
    return visited
    

a = int(input())
graph = dict()
for i in range(a):
    lst = list(input().split())
    graph[lst[0]] = lst[1:]
print("".join(preorder(graph,'A')))
print("".join(inorder(graph,'A')))
print("".join(postorder(graph,'A')))