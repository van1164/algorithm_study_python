from collections import deque
def bfs(graph):
    visited = {1}
    stack = deque([1])
    answer = 0
    while True:
        blank_stack = deque()
        while stack:
            n = stack.popleft()
            for i in range(1,7):
                temp = i +n
                if temp not in visited:
                    if temp in graph:
                        visited.add(temp)
                        visited.add(graph[temp])
                        blank_stack.append(graph[temp])
                    else:
                        blank_stack.append(temp)
                        visited.add(temp)
        stack = blank_stack
        answer +=1
        if 100 in visited:
            break
    return answer      
a,b = list(map(int,input().rstrip().split()))
lst={}
for i in range(a+b):
    a,b = list(map(int,input().rstrip().split()))
    lst[a] =b
print(bfs(lst))